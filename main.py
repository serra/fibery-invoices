import os
import click
import requests

invoice_query = """
    {
      findInvoices(state: {name: {is: "%s"}}) {
        invoiceNumber
        customerName
        customerAddress
        customerZipcode
        customerCity
        invoiceDate
        dueDate
        totalAmount
        invoiceLines {
          name
          quantity
          unitPrice
          totalPrice
        }
      }
    }
    """


@click.command()
@click.option("--state", default="Ready", help="Filter invoices by state")
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--token", envvar="FIBERY_API_TOKEN", help="Fibery API Token")
def list_invoices(state, url, token):
    query = invoice_query % state

    headers = {"Content-Type": "application/json", "Authorization": "Token " + token}

    response = requests.post(url, json={"query": query}, headers=headers)
    invoice_data = response.json()["data"]["findInvoices"]
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of {invoice['totalAmount']} for {invoice['customerName']} is {state}"
        )


if __name__ == "__main__":
    list_invoices()
