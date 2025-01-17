import pathlib
from iso4217 import Currency
from swissqr import PaymentParty, QRData, SwissQR

# Create a PaymentParty object for the payment receiver
p = PaymentParty(
    name="Hambone Fakenamington",
    street="Madeup Street",
    street_no="1",
    zipcode="9999",
    city="Madeup Town",
    country="CH"
)

# Create QR code data model
d = QRData(
    iban="CH1234567890123456789",
    creditor=p,
    amount=5.0,
    currency=Currency.chf,
    message="Have a beer!"
)

# Create QR code object
q = SwissQR(d)

# Get QR code svg as a string
markup = q.get_markup()

# Save QR code to a file
p = pathlib.Path("/tmp/qr.svg")
q.save(p)