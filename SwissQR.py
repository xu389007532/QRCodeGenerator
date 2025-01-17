import qrbill
from qrbill import QRBill

#language='en', 'de', 'fr' or 'it'
# ('street', 'house_num', 'pcode', 'city') ="S"
# ('line1','line2') ="K"

creditor_name='DodoBahati Stiftung für den Schutz der letzten Wildtiere'
creditor_pcode="8967"
creditor_city='Widen'
creditor_country='CH'
creditor={'name': creditor_name, 'street':None,'pcode': creditor_pcode, 'city': creditor_city, 'country': creditor_country}


debtor_name='Ruth Zeiter'
debtor_line1="Birkenweg"
debtor_line2='3930 Visp'
debtor_country='CH'
debtor={'name': debtor_name, 'line1':debtor_line1, 'line2': debtor_line2, 'country': debtor_country}

my_bill = QRBill(
    account='CH4730000001611650930',
    creditor=creditor,
    # creditor={'name': 'DodoBahati Stiftung für den Schutz der letzten Wildtiere', 'pcode': '8967', 'city': 'Widen', 'country': 'CH'},
    currency="CHF",
    amount=None,    #amount=None 或者字符類型的數字. 例如: None, "1", "2.5"
    language="it",  #'en', 'de', 'fr' or 'it'
    # debtor={'name': 'Ruth Zeiter', 'street':'Birkenweg', 'house_num':'2b', 'pcode': '3930', 'city': 'Visp', 'country': 'CH'},
    # debtor={'name': 'Ruth Zeiter', 'line1':'Birkenweg', 'line2': '3930 Visp', 'country': 'CH'},
    debtor=debtor,
    reference_number="000000000000010000321598160",
    additional_information="",
    top_line=False,
    payment_line=False,
    font_factor=1,      #0 就不輸出文字, 1 輸出字體
    )


my_bill.as_svg('PaymentPart_it_test1.svg')

# my_bill.qr_image()
