"""Editable site content. Replace placeholders here; templates need no changes."""

COMPANY = {
    "name": "Afritensor Consult",
    "tagline": "Finance, technology, tax and training expertise under one firm.",
    "description": ("Afritensor Consult is a multidisciplinary professional services firm "
                    "supporting organisations in finance and audit, technology and data, "
                    "debt management, taxation and payroll, and corporate training."),
    # To use the real logo: put the file in static/img/ and set e.g. "logo_image": "img/logo.svg"
    "logo_image": None,
    "address": "[Office address]",
    "phone": "[Telephone number]",
    "email": "[Email address]",
    "hours": "[Business hours]",
    "social": [  # add {"label": "LinkedIn", "url": "https://..."} when available
        {"label": "LinkedIn", "url": None},
        {"label": "X (Twitter)", "url": None},
        {"label": "Facebook", "url": None},
    ],
}

SERVICES = [
    {"slug": "finance-audit", "title": "Finance & Audit",
     "summary": "Support for sound financial practice, reporting, internal controls and decision-making.",
     "detail": "We help organisations maintain reliable financial records and make well-informed decisions.",
     "scope": ["Financial reporting and accounting support", "Internal audit and control reviews",
               "External audit preparation", "Management reporting and analysis"]},
    {"slug": "software-data", "title": "Software Development & Data Analysis",
     "summary": "Software and data solutions built around real business requirements.",
     "detail": "We design and build systems that fit how an organisation actually works.",
     "scope": ["Custom software development", "Data analysis and reporting",
               "Dashboards and data visualisation", "Business intelligence", "Process automation"]},
    {"slug": "debt-management", "title": "Debt Management & Collection",
     "summary": "Structured support for receivables, credit control and recovery.",
     "detail": "We help organisations protect cash flow through disciplined credit and collection processes.",
     "scope": ["Receivables management", "Credit control", "Recovery processes",
               "Account monitoring", "Collection reporting"]},
    {"slug": "tax-payroll", "title": "Taxation & Payroll Consultancy",
     "summary": "Guidance on tax matters, payroll processes and statutory compliance.",
     "detail": "We help organisations meet their obligations accurately and on time.",
     "scope": ["Tax advisory and compliance support", "Payroll processing and review",
               "Statutory reporting", "Payroll systems support"]},
    {"slug": "corporate-training", "title": "Corporate Training",
     "summary": "Practical programmes that build capability inside your organisation.",
     "detail": "Training is tailored to the audience and delivered around real working situations.",
     "scope": ["Finance and accounting", "Taxation", "Technology and data",
               "Management", "Other business capabilities"]},
]

DIRECTORS = [  # photo: filename in static/img/directors/ (None shows a neutral placeholder)
    {"name": "[Director Name]", "role": "Managing Director", "photo": None,
     "bio": "[Professional biography to be supplied.]"},
    {"name": "[Director Name]", "role": "Finance & Audit Director", "photo": None,
     "bio": "[Professional biography to be supplied.]"},
    {"name": "[Director Name]", "role": "Technology & Data Director", "photo": None,
     "bio": "[Professional biography to be supplied.]"},
    {"name": "[Director Name]", "role": "Tax & Corporate Advisory Director", "photo": None,
     "bio": "[Professional biography to be supplied.]"},
]

VALUES = [
    ("Integrity", "We give advice we can stand behind and report findings as they are."),
    ("Precision", "Numbers, code and documents are checked before they leave our hands."),
    ("Practicality", "Recommendations are built to be implemented by the people who must use them."),
    ("Confidentiality", "Client information is handled with discretion at every stage."),
]
