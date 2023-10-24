# Fibery invoices automation

This repository contains scripts that help me automate my Fibery invoice workflows.

I use the Fibery [GraphQL API] to access data.

The app will fetch invoice data from my Fibery workspace. Fibery is an online collaboration and knowledge management system. In Fibery, information is stored in an unstructured (markdown) format and in a structured, relational database-like format. The structured information is available through a GraphQL api.

## Set up environment

```
make bootstrap
. ./venv/bin/activate
make update
```

## How to use

Set the `FIBERY_API_TOKEN` environment variable to your API key.
I use 1password: `. ./export_api_token_from_1password.sh`.

```
make console
```

## Features

* List open invoices ready to be sent.
* Generate pdf invoices matching the style of our public website.

---

## Doing

* Save email to draft box in Google workspace.

## Backlog

* Upload the pdf to Fibery.
* Upload the invoice to the administration.
* Find a way to use local resources only.

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
