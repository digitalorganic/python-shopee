from .base import BaseModule



class Payment(BaseModule):
    
    def get_transaction_list(self, **kwargs):
        """
        GetTransactionList: Use this API to get the transaction records of wallet.
        https://open.shopee.com/documents?module=69&type=1&id=457

        """
        return self.client.execute("wallet/transaction/list", "POST", kwargs)

    def get_payout_details(self, **kwargs):
        """
        GetTransactionList: Use this API to get the transaction records of wallet.
        https://open.shopee.com/documents?module=69&type=1&id=467
        """
        return self.client.execute("payment/get_payout_details", "POST", kwargs)