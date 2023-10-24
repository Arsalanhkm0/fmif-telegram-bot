<?php

// تنظیم توکن API بات خود در اینجا
define('6061209511:AAG2swGekiaUdUdPz5xANYsRTk4wpvuiZk0');

// آدرس انتهایی API تلگرام
// define('API_URL', 'https://api.telegram.org/bot' . API_TOKEN . '/');

// دریافت داده‌های پیام ورودی
$update = json_decode(file_get_contents('php://input'), true);

// دریافت شناسه چت و متن پیام
$chatID = $update['message']['chat']['id'];
$message = $update['message']['text'];

// پردازش دستورات
if ($message == '/start') {
    sendMessage($chatID, 'خوش آمدید! برای دریافت سلامی، /hello را تایپ کنید.');
} elseif ($message == '/hello') {
    sendMessage($chatID, 'سلام! چطور می‌توانم به شما کمک کنم؟');
} elseif ($message == '/time') {
    // دریافت زمان فعلی سرور و ارسال آن به کاربر
    sendMessage($chatID, 'زمان فعلی سرور: ' . date('Y-m-d H:i:s'));
} else {
    sendMessage($chatID, 'دستور نامعتبر. برای شروع، /start را تایپ کنید.');
}

// تابع ارسال پیام به کاربر
function sendMessage($chatID, $message) {
    $url = API_URL . 'sendMessage?chat_id=' . $chatID . '&text=' . urlencode($message);
    file_get_contents($url);
}

?>
