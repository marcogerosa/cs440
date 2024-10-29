class NotificationSystem:
    def __init__(self):
        self.email_sender = EmailService()
        self.sms = SMSProvider()
        self.push_notifications = PushNotificationManager()
        self.message_log = []

    def send_email(self, to_address, subject, body):
        try:
            self.email_sender.dispatch_email_message(
                to_address, 
                subject, 
                body,
                priority="normal"
            )
            self._log("email", "sent", to_address)
        except Exception as e:
            self._log("email", "failed", str(e))

    def sendSMS(self, phone_num, message): 
        if self._validate_phone(phone_num):
            self.sms.send(phone_num, message)
            self._log("sms", "delivered", phone_num) 
        else:
            self._log("sms", "invalid number", phone_num)

    def push_message(self, user_id, text, platform): 
        if platform in ["ios", "android"]: 
            self.push_notifications.push(
                userId=user_id,
                message_body=text,
                platform_type=platform
            )
            self._log("push", "success", user_id)  
        else:
            self._log("push", "invalid platform", platform)

    def _validate_phone(self, number):
        return len(number) >= 10 and number.isdigit()

    def _log(self, type, status, details):
        self.message_log.append({
            "type": type,
            "status": status,
            "details": details,
            "timestamp": datetime.now()
        })

    def get_notification_history(self, type=None):
        if type:
            return [log for log in self.message_log if log["type"] == type]
        return self.message_log
    
