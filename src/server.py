import xml.etree.ElementTree as ET
class PaymentServer:
    def handle(self, payment_message_request_xml: str) -> str:
        self.parse_transaction(payment_message_request_xml)
        customer = self.get_customer(self.get_token())
        return self.check_conditions(customer)
    def __init__(self, customers: list) -> None:
        self.customers = customers
        self.req = None
        self.transaction_dates = {cust['card_token']: [] for cust in customers}
    def parse_transaction(self, transaction: str) -> None:
        tree = ET.parse(transaction)
        root = tree.getroot()
        self.req = root.find('Transaction')
    def get_token(self) -> str | None:
        token = self.req.find('Token')
        if token is None:
            return None
        return token.text
    def get_amount(self) -> int | None:
        amount = self.req.find('Amount')
        if amount is None:
            return None
        return int(amount.text)
    def get_customer(self, token: str) -> dict | None:
        for customer in self.customers:
            if token == customer['card_token']:
                return customer
        return None
    def create_response(self, result: str, reason: str):
        body = ET.Element('Body')
        response = ET.SubElement(body, 'TransactionResponse')
        ET.SubElement(response, 'Result').text = result
        ET.SubElement(response, 'Reason').text = reason
        tree = ET.ElementTree(body)
        return tree
    def check_conditions(self, customer):
        if customer is None:
            return self.create_response('decline', '')
        transaction_amount = self.get_amount()
        if customer['Limit'] > transaction_amount:
            if transaction_amount > 150:
                return self.create_response('decline', 'TransactionAmountOverLimit')
            customer['Limit'] = customer['Limit'] - transaction_amount
            return self.create_response('accept', '')
        else:
            return self.create_response('decline', 'InsufficientFunds')
def main() -> None:
    with open('resources/limits', 'r') as file:
        my_line = file.readline().split(',')
        my_line = [item.strip()[1:-1] for item in my_line]
        customers = []
        for line in file:
            line = line.split(',')
            line = [item.strip()[1:-1] for item in line]
            customers.append({my_line[0]: int(line[0]),
                              my_line[1]: line[1],
                              my_line[2]: line[2],
                              my_line[3]: line[3],
                              my_line[4].strip(): line[4]
                              }
                             )
    server = PaymentServer(customers)
    file_names = [f'resources/payments/payment_{i}.xml' for i in range(1, 21)]
    for file_name in file_names:
        with open(file_name, 'r') as file:
            response = server.handle(file)
        name = file_name.split('.')[0]
        response.write(f'{name}_response.xml')

if __name__ == '__main__':
    main()