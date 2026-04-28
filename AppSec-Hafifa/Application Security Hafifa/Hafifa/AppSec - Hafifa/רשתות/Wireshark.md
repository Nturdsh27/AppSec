# **Wireshark :**

Wireshark היא אפליקצייה המשמשת ל"תפיסת" פאקטות שעוברות ברשת ומאפשרת לעשות אנליזה לכל אחת מהפאקטות בנפרד , הוא מאפשר לקחת מכרטיס הרשת את המידע שזורם ומציג אותם בצורה מובנת יותר לעין , זה נעשה על ידי יירוט של התעבורה הרשתית בדיקת הheaderים והpayloadים , פיענוח הפרוטוקולים , הוצאת המידע הרלוונטי וכתיבתן.

![תמונות](../../Attachments/attachment_23.png)

## **זיהוי השדות בפאקטת HTTP:**

Frame:

![תמונות](../../Attachments/attachment_24.png)

Packet:

![תמונות](../../Attachments/attachment_25.png)

TCP Header:

![תמונות](../../Attachments/attachment_26.png)

HTTP Payload :

![תמונות](../../Attachments/attachment_27.png)

## **Pcap 1:**

חשוד

![תמונות](../../Attachments/attachment_28.png)![תמונות](../../Attachments/attachment_29.png)![תמונות](../../Attachments/attachment_30.png)יש ניסיון של brute force למשתמש בשם : bro עם סיסמאות של המספרים בין 1-31 לתוך שרת FTP בניסון להכנס כמשתמש FTP.

EFDIBI

## **A.pcap :**

ARP Spoofing

תיאור כללי על הpcap:

יש ARP SPOOFING מכתובת 192.168.1.105 על כתובת 192.168.1.104 , 192.168.1.105גורם ל192.168.1.104 לחשוב שהוא 192.168.1.1.

![תמונות](../../Attachments/attachment_31.png)

## **B pcap :**

חשוד

![תמונות](../../Attachments/attachment_32.png)נעשית שליחה של הודעות לSYN לכל מיני פורט של פרוטוקולים ידועים על מנת למצוא איזה מהם פתוח , כלומר נעשה פה port scan לפורטים ידועים.

## **C.pacp :**

לא חשוד

![תמונות](../../Attachments/attachment_33.png)ניתן לראות את הטלפון של ניקיטה קומלייב התוקף הרוסי הידוע לשמצא

![תמונות](../../Attachments/attachment_34.png)מעבר של תעודה דיגיטלית

![תמונות](../../Attachments/attachment_35.png)
