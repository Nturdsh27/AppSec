# **Wireshark :**

<div dir="rtl">Wireshark היא אפליקצייה המשמשת ל"תפיסת" פאקטות שעוברות ברשת ומאפשרת לעשות אנליזה לכל אחת מהפאקטות בנפרד , הוא מאפשר לקחת מכרטיס הרשת את המידע שזורם ומציג אותם בצורה מובנת יותר לעין , זה נעשה על ידי יירוט של התעבורה הרשתית בדיקת הheaderים והpayloadים , פיענוח הפרוטוקולים , הוצאת המידע הרלוונטי וכתיבתן.</div>

![תמונות](../Attachments/attachment_23.png)

## <div dir="rtl"><strong>זיהוי השדות בפאקטת HTTP:</strong></div>

Frame:

![תמונות](../Attachments/attachment_24.png)

Packet:

![תמונות](../Attachments/attachment_25.png)

TCP Header:

![תמונות](../Attachments/attachment_26.png)

HTTP Payload :

![תמונות](../Attachments/attachment_27.png)

## **Pcap 1:**

<div dir="rtl">חשוד</div>

<div dir="rtl"><img src="../Attachments/attachment_28.png" alt="תמונות"><img src="../Attachments/attachment_29.png" alt="תמונות"><img src="../Attachments/attachment_30.png" alt="תמונות">יש ניסיון של brute force למשתמש בשם : bro עם סיסמאות של המספרים בין 1-31 לתוך שרת FTP בניסון להכנס כמשתמש FTP.</div>

EFDIBI

## **A.pcap :**

ARP Spoofing

<div dir="rtl">תיאור כללי על הpcap:</div>

<div dir="rtl">יש ARP SPOOFING מכתובת 192.168.1.105 על כתובת 192.168.1.104 , 192.168.1.105גורם ל192.168.1.104 לחשוב שהוא 192.168.1.1.</div>

![תמונות](../Attachments/attachment_31.png)

## **B pcap :**

<div dir="rtl">חשוד</div>

<div dir="rtl"><img src="../Attachments/attachment_32.png" alt="תמונות">נעשית שליחה של הודעות לSYN לכל מיני פורט של פרוטוקולים ידועים על מנת למצוא איזה מהם פתוח , כלומר נעשה פה port scan לפורטים ידועים.</div>

## **C.pacp :**

<div dir="rtl">לא חשוד</div>

<div dir="rtl"><img src="../Attachments/attachment_33.png" alt="תמונות">ניתן לראות את הטלפון של ניקיטה קומלייב התוקף הרוסי הידוע לשמצא</div>

<div dir="rtl"><img src="../Attachments/attachment_34.png" alt="תמונות">מעבר של תעודה דיגיטלית</div>

![תמונות](../Attachments/attachment_35.png)
