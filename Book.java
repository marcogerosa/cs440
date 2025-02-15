import java.util.ArrayList;
import java.util.List;
 
class Author {
	private String name;
	private List<Book> books;
 
	public Author(String name) {
    	this.name = name;
    	this.books = new ArrayList<>();
	}
 
	public Book writeBook(String title, String isbn, double price) {
    	Book book = new Book(title, isbn, price, this);
    	books.add(book);
    	return book;
	}
 
	public String getName() {
    	return name;
	}
 
	public List<Book> getBooks() {
    	return books;
	}
}
 
class Book {
	private String title;
	private String isbn;
	private double price;
	private List<Author> authors;
 
	public Book(String title, String isbn, double price, Author author) {
    	this.title = title;
    	this.isbn = isbn;
    	this.price = price;
    	this.authors = new ArrayList<>();
    	this.authors.add(author);
	}
 
	public void addAuthor(Author author) {
    	authors.add(author);
    	author.getBooks().add(this);
	}
 
	public String getTitle() {
    	return title;
	}
 
	public String getIsbn() {
    	return isbn;
	}
 
	public double getPrice() {
    	return price;
	}
 
	public List<Author> getAuthors() {
    	return authors;
	}
}
 
class Customer {
	private String name;
	private String email;
 
	public Customer(String name, String email) {
    	this.name = name;
    	this.email = email;
	}
 
	public ShoppingCart createShoppingCart() {
    	return new ShoppingCart(this);
	}
 
	public String getName() {
    	return name;
	}
 
	public String getEmail() {
    	return email;
	}
}
class ShoppingCart {
	private Customer customer;
	private List<Item> items;
 
	public ShoppingCart(Customer customer) {
    	this.customer = customer;
    	this.items = new ArrayList<>();
	}
 
	public void addBook(Book book, int quantity) {
    	items.add(new Item(book, quantity));
	}
 
	public void removeBook(Book book) {
    	items.removeIf(item -> item.getBook().equals(book));
	}
 
	public Order checkout() {
    	Order order = new Order(customer, new ArrayList<>(items));
    	items.clear();
    	return order;
	}
 
	public List<Item> getItems() {
    	return items;
	}
}
 
class Item {
	private Book book;
	private int quantity;
 
	public Item(Book book, int quantity) {
    	this.book = book;
    	this.quantity = quantity;
	}
 
	public Book getBook() {
    	return book;
	}
 
	public int getQuantity() {
    	return quantity;
	}
}
 
class Order {
	private Customer customer;
	private List<Item> items;
	private String status;
 
	public Order(Customer customer, List<Item> items) {
    	this.customer = customer;
    	this.items = items;
    	this.status = "New";
	}
 
	public void processOrder() {
    	this.status = "Processing";
	}
 
	public void shipOrder() {
    	this.status = "Shipped";
	}
 
	public void deliverOrder() {
    	this.status = "Delivered";
	}
 
	public String getStatus() {
    	return status;
	}
 
	public List<Item> getItems() {
    	return items;
	}
 
	public Customer getCustomer() {
    	return customer;
	}
}


