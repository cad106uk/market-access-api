# Generated by Django 2.0.5 on 2018-09-28 13:26

from django.db import migrations

# Generated by Django 2.0.5 on 2018-09-21 10:30

from django.db import migrations

actual_dummies_to_add = [
    {
        "title": "Locally produced material in goods",
        "description": "The requirement that goods contain a high proportion of locally produced material.",
        "category": "GOODS",
    },
    {
        "title": "Restrictions on live animals, or animal and plant products",
        "description": "<p>These sanitary and phytosanitary measures are implemented to protect human, animal, or plant health life. Threats to human, animal or plant health could arise from:</p><li>additives</li><li>contaminants</li><li>toxins</li><li>disease-causing organisms</li>",
        "category": "GOODS",
    },
    {
        "title": "Environmental regulations on goods",
        "description": "Restrictions on goods that could be harmful to the environment of the country the goods are being exported to.",
        "category": "GOODS",
    },
    {
        "title": "Safety regulations on goods",
        "description": "Restrictions of imports of products from countries or regions where there is a lack of evidence of sufficient safety conditions.",
        "category": "GOODS",
    },
    {
        "title": "Quality measures on goods",
        "description": "<p>Conditions of performance of goods, for example durability or hardness or quality of goods, for example content of defined ingredients.<br>These measures include:</p><li>product definitions</li><li>grading standards</li><li>production or processing regulations</li>",
        "category": "GOODS",
    },
    {
        "title": "Packaging, labelling or design regulations",
        "description": "Measures defining the information and packaging which should be provided to the consumer.",
        "category": "GOODS",
    },
    {
        "title": "Import quotas",
        "description": "Limits on the amount of a good that can be imported into a country. ",
        "category": "GOODS",
    },
    {
        "title": "Customs procedures",
        "description": "Requirements that goods go through checks, or licences are secured before being imported.",
        "category": "GOODS",
    },
    {
        "title": "Rules of origin",
        "description": "Issues related to countries requiring evidence which shows the country a good was made in.",
        "category": "GOODS",
    },
    {
        "title": "Restrictions on internal distribution",
        "description": "Restrictions on internal distribution of a good being imported into a country. For example, in the US, transhipment can only be undertaken by US vessels, movement of some goods across or between states is subject to labour and union rules.",
        "category": "GOODS",
    },
    {
        "title": "Restrictions on foreign entry or movement of people",
        "description": "<p>This includes:</p><li>visa costs</li><li>difficulties getting visas to do business</li><li>residence or nationality requirements</li><li>restrictions on buying land as foreign service supplier</li>",
        "category": "SERVICES",
    },
    {
        "title": "Local presence requirements",
        "description": "Requirements for a service supplier to be a resident or from an enterprise in the country in which you are supplying a service.",
        "category": "SERVICES",
    },
    {
        "title": "Fees that only apply to foreign service suppliers",
        "description": "Policies that favour domestic service suppliers by placing unnecessary charges on foreign suppliers",
        "category": "SERVICES",
    },
    {
        "title": "Restrictions on type of business, legal entity or joint venture that suppliers can operate under",
        "description": "Requirements on businesses to have certain structures when operating in a country, or disadvantages to businesses with different structures.",
        "category": "SERVICES",
    },
    {
        "title": "Limitations on access to key infrastructure",
        "description": "For example, barriers to foreign service suppliers being able to open a local bank account or register websites with a local domain name",
        "category": "SERVICES",
    },
    {
        "title": "Restrictions on foreign suppliers",
        "description": "<p>Limits on the value or amount of services that can be supplied, the number of employees that suppliers can have, or the number of suppliers allowed in the market.</p><p>For example, this could be limits in the form of quotas or the requirement for businesses to fulfil certain conditions in order to obtain market access</p>",
        "category": "SERVICES",
    },
    {
        "title": "Qualification requirements",
        "description": "Requirements for qualifications specific to the country you export to or qualifications not being recognised in the country you export to",
        "category": "SERVICES",
    },
    {
        "title": "Tariffs and taxes imposed to protect or favour local suppliers",
        "description": "Import duties or taxes, other than tariffs, that favour domestic firms over foreign competitors. These can be placed on imports to make them more expensive than domestically produced goods.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Government subsidies",
        "description": "Transfers of public funds to specific companies, sectors or regions which artificially lower prices and distort competition. This could include preferential tax arrangements.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Restrictions on how much money you can invest into a country",
        "description": "Restrictions on the amount of money a supplier can invest in a country they are exporting to.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Government procurement restrictions",
        "description": "Regulations which encourage that a government buys goods or services from domestic suppliers. This can make it difficult for non-domestic suppliers to compete for a contract or for non-domestic goods and services to be used.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Price controls",
        "description": "Measures to control the price of imported goods. These can be used to support the price of domestic products when import prices are lower.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Enforcement, or lack of enforcement, of rules and regulations",
        "description": "A country that lacks any regulatory measures for products or services, or does not comply with international regulations like the WTO’s regulations.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Unfair application of competition rules",
        "description": "Competition law that is applied in an unfair way to target foreign firms or to protect domestic firms. This could include the failure to properly enforce competition law, or a lack of procedural rights for businesses to get a fair hearing.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "State-granted monopolies or exclusive rights",
        "description": "A government granting one or more private companies the legal right to be the only operator in a market.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "State-owned enterprises",
        "description": "Unfair advantages to state-owned companies, such as special rights or privileges, government funding, or exemptions from laws and regulations.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Restrictions on local assets, local components or to train local workers",
        "description": "Restrictions requiring you to use local assets, components or workers when operating in a country.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Intellectual property rights and regulations",
        "description": "<p>This includes trade related intellectual property legislation and covers:<li>patents</li><li>trademarks</li><li>industrial designs</li><li>layout designs of integrated circuits</li><li>copyright</li><li>geographical indications</li><li>trade secrets</li></p>",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Difficulties in accessing data",
        "description": "Barriers to accessing data on regulations and procedures or points of contact.",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Restrictions on storing/sending data across countries",
        "description": "Any barriers to the flow of data into countries in which you are supplying a service, as well as data localisation requirements or similar",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Testing, inspection and certification procedures",
        "description": "Requirement to complete conformity assessments to show produce complies with technical regulations or standards",
        "category": "GOODSANDSERVICES",
    },
    {
        "title": "Restrictions on business names",
        "description": "Restrictions on the operation of service suppliers under the business name",
        "category": "GOODSANDSERVICES",
    },
]

def clear_barrier_types(apps, schema_editor):
    BarrierType = apps.get_model("metadata", "BarrierType")
    BarrierType.objects.all().delete()

def add_actual_barrier_types(apps, schema_editor):
    BarrierType = apps.get_model("metadata", "BarrierType")

    for item in actual_dummies_to_add:
        try:
            barrier_type = BarrierType.objects.get(title=item["title"])
            barrier_type.description = item["description"]
            barrier_type.category = item["category"]
            barrier_type.save()
        except BarrierType.DoesNotExist:
            BarrierType(
                title=item["title"],
                description=item["description"],
                category=item["category"],
            ).save()



class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0007_auto_20180921_1030'),
    ]

    operations = [
        migrations.RunPython(clear_barrier_types),
        migrations.RunPython(add_actual_barrier_types),
    ]
