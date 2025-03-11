class OrderProcessor {
    public void processOrder(Order order) {
        // Validate the order
        if (order.getItems().isEmpty()) {
            throw new IllegalArgumentException("Order has no items");
        }
        
        // Calculate total
        double total = 0;
        for (Item item : order.getItems()) {
            total += item.getPrice() * item.getQuantity();
        }
        order.setTotal(total);
        
        // Apply discount
        if (order.getCustomer().isVIP()) {
            double discount = total * 0.1;
            order.setDiscount(discount);
            order.setFinalTotal(total - discount);
        } else {
            order.setFinalTotal(total);
        }
        
        // Update inventory
        for (Item item : order.getItems()) {
            Inventory inventory = getInventoryRepository().findByProductId(item.getProductId());
            inventory.decreaseStock(item.getQuantity());
            getInventoryRepository().save(inventory);
        }
        
        // Charge payment
        PaymentGateway gateway = new PaymentGateway();
        PaymentResult result = gateway.charge(order.getCustomer().getCreditCard(), order.getFinalTotal());
        if (!result.isSuccess()) {
            throw new PaymentFailedException(result.getErrorMessage());
        }
        
        // Update order status
        order.setStatus("PAID");
        getOrderRepository().save(order);
        
        // Send confirmation email
        EmailService emailService = new EmailService();
        String subject = "Order Confirmation: " + order.getId();
        String body = "Thank you for your order. Your order #" + order.getId() + " has been placed.";
        emailService.sendEmail(order.getCustomer().getEmail(), subject, body);
        
        // Generate shipping label
        ShippingLabelGenerator labelGenerator = new ShippingLabelGenerator();
        ShippingLabel label = labelGenerator.generateLabel(order);
        
        // Log order completion
        System.out.println("Order " + order.getId() + " processed successfully");
    }
    
    private OrderRepository getOrderRepository() {
        // Return order repository
        return new OrderRepository();
    }
    
    private InventoryRepository getInventoryRepository() {
        // Return inventory repository
        return new InventoryRepository();
    }
}
