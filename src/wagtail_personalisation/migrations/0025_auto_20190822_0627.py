# Generated by Django 2.1.11 on 2019-08-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_personalisation", "0024_origincountryrule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="origincountryrule",
            name="country",
            field=models.CharField(
                choices=[
                    ("aw", "Aruba"),
                    ("af", "Afghanistan"),
                    ("ao", "Angola"),
                    ("ai", "Anguilla"),
                    ("ax", "Åland Islands"),
                    ("al", "Albania"),
                    ("ad", "Andorra"),
                    ("ae", "United Arab Emirates"),
                    ("ar", "Argentina"),
                    ("am", "Armenia"),
                    ("as", "American Samoa"),
                    ("aq", "Antarctica"),
                    ("tf", "French Southern Territories"),
                    ("ag", "Antigua and Barbuda"),
                    ("au", "Australia"),
                    ("at", "Austria"),
                    ("az", "Azerbaijan"),
                    ("bi", "Burundi"),
                    ("be", "Belgium"),
                    ("bj", "Benin"),
                    ("bq", "Bonaire, Sint Eustatius and Saba"),
                    ("bf", "Burkina Faso"),
                    ("bd", "Bangladesh"),
                    ("bg", "Bulgaria"),
                    ("bh", "Bahrain"),
                    ("bs", "Bahamas"),
                    ("ba", "Bosnia and Herzegovina"),
                    ("bl", "Saint Barthélemy"),
                    ("by", "Belarus"),
                    ("bz", "Belize"),
                    ("bm", "Bermuda"),
                    ("bo", "Bolivia, Plurinational State of"),
                    ("br", "Brazil"),
                    ("bb", "Barbados"),
                    ("bn", "Brunei Darussalam"),
                    ("bt", "Bhutan"),
                    ("bv", "Bouvet Island"),
                    ("bw", "Botswana"),
                    ("cf", "Central African Republic"),
                    ("ca", "Canada"),
                    ("cc", "Cocos (Keeling) Islands"),
                    ("ch", "Switzerland"),
                    ("cl", "Chile"),
                    ("cn", "China"),
                    ("ci", "Côte d'Ivoire"),
                    ("cm", "Cameroon"),
                    ("cd", "Congo, The Democratic Republic of the"),
                    ("cg", "Congo"),
                    ("ck", "Cook Islands"),
                    ("co", "Colombia"),
                    ("km", "Comoros"),
                    ("cv", "Cabo Verde"),
                    ("cr", "Costa Rica"),
                    ("cu", "Cuba"),
                    ("cw", "Curaçao"),
                    ("cx", "Christmas Island"),
                    ("ky", "Cayman Islands"),
                    ("cy", "Cyprus"),
                    ("cz", "Czechia"),
                    ("de", "Germany"),
                    ("dj", "Djibouti"),
                    ("dm", "Dominica"),
                    ("dk", "Denmark"),
                    ("do", "Dominican Republic"),
                    ("dz", "Algeria"),
                    ("ec", "Ecuador"),
                    ("eg", "Egypt"),
                    ("er", "Eritrea"),
                    ("eh", "Western Sahara"),
                    ("es", "Spain"),
                    ("ee", "Estonia"),
                    ("et", "Ethiopia"),
                    ("fi", "Finland"),
                    ("fj", "Fiji"),
                    ("fk", "Falkland Islands (Malvinas)"),
                    ("fr", "France"),
                    ("fo", "Faroe Islands"),
                    ("fm", "Micronesia, Federated States of"),
                    ("ga", "Gabon"),
                    ("gb", "United Kingdom"),
                    ("ge", "Georgia"),
                    ("gg", "Guernsey"),
                    ("gh", "Ghana"),
                    ("gi", "Gibraltar"),
                    ("gn", "Guinea"),
                    ("gp", "Guadeloupe"),
                    ("gm", "Gambia"),
                    ("gw", "Guinea-Bissau"),
                    ("gq", "Equatorial Guinea"),
                    ("gr", "Greece"),
                    ("gd", "Grenada"),
                    ("gl", "Greenland"),
                    ("gt", "Guatemala"),
                    ("gf", "French Guiana"),
                    ("gu", "Guam"),
                    ("gy", "Guyana"),
                    ("hk", "Hong Kong"),
                    ("hm", "Heard Island and McDonald Islands"),
                    ("hn", "Honduras"),
                    ("hr", "Croatia"),
                    ("ht", "Haiti"),
                    ("hu", "Hungary"),
                    ("id", "Indonesia"),
                    ("im", "Isle of Man"),
                    ("in", "India"),
                    ("io", "British Indian Ocean Territory"),
                    ("ie", "Ireland"),
                    ("ir", "Iran, Islamic Republic of"),
                    ("iq", "Iraq"),
                    ("is", "Iceland"),
                    ("il", "Israel"),
                    ("it", "Italy"),
                    ("jm", "Jamaica"),
                    ("je", "Jersey"),
                    ("jo", "Jordan"),
                    ("jp", "Japan"),
                    ("kz", "Kazakhstan"),
                    ("ke", "Kenya"),
                    ("kg", "Kyrgyzstan"),
                    ("kh", "Cambodia"),
                    ("ki", "Kiribati"),
                    ("kn", "Saint Kitts and Nevis"),
                    ("kr", "Korea, Republic of"),
                    ("kw", "Kuwait"),
                    ("la", "Lao People's Democratic Republic"),
                    ("lb", "Lebanon"),
                    ("lr", "Liberia"),
                    ("ly", "Libya"),
                    ("lc", "Saint Lucia"),
                    ("li", "Liechtenstein"),
                    ("lk", "Sri Lanka"),
                    ("ls", "Lesotho"),
                    ("lt", "Lithuania"),
                    ("lu", "Luxembourg"),
                    ("lv", "Latvia"),
                    ("mo", "Macao"),
                    ("mf", "Saint Martin (French part)"),
                    ("ma", "Morocco"),
                    ("mc", "Monaco"),
                    ("md", "Moldova, Republic of"),
                    ("mg", "Madagascar"),
                    ("mv", "Maldives"),
                    ("mx", "Mexico"),
                    ("mh", "Marshall Islands"),
                    ("mk", "North Macedonia"),
                    ("ml", "Mali"),
                    ("mt", "Malta"),
                    ("mm", "Myanmar"),
                    ("me", "Montenegro"),
                    ("mn", "Mongolia"),
                    ("mp", "Northern Mariana Islands"),
                    ("mz", "Mozambique"),
                    ("mr", "Mauritania"),
                    ("ms", "Montserrat"),
                    ("mq", "Martinique"),
                    ("mu", "Mauritius"),
                    ("mw", "Malawi"),
                    ("my", "Malaysia"),
                    ("yt", "Mayotte"),
                    ("na", "Namibia"),
                    ("nc", "New Caledonia"),
                    ("ne", "Niger"),
                    ("nf", "Norfolk Island"),
                    ("ng", "Nigeria"),
                    ("ni", "Nicaragua"),
                    ("nu", "Niue"),
                    ("nl", "Netherlands"),
                    ("no", "Norway"),
                    ("np", "Nepal"),
                    ("nr", "Nauru"),
                    ("nz", "New Zealand"),
                    ("om", "Oman"),
                    ("pk", "Pakistan"),
                    ("pa", "Panama"),
                    ("pn", "Pitcairn"),
                    ("pe", "Peru"),
                    ("ph", "Philippines"),
                    ("pw", "Palau"),
                    ("pg", "Papua New Guinea"),
                    ("pl", "Poland"),
                    ("pr", "Puerto Rico"),
                    ("kp", "Korea, Democratic People's Republic of"),
                    ("pt", "Portugal"),
                    ("py", "Paraguay"),
                    ("ps", "Palestine, State of"),
                    ("pf", "French Polynesia"),
                    ("qa", "Qatar"),
                    ("re", "Réunion"),
                    ("ro", "Romania"),
                    ("ru", "Russian Federation"),
                    ("rw", "Rwanda"),
                    ("sa", "Saudi Arabia"),
                    ("sd", "Sudan"),
                    ("sn", "Senegal"),
                    ("sg", "Singapore"),
                    ("gs", "South Georgia and the South Sandwich Islands"),
                    ("sh", "Saint Helena, Ascension and Tristan da Cunha"),
                    ("sj", "Svalbard and Jan Mayen"),
                    ("sb", "Solomon Islands"),
                    ("sl", "Sierra Leone"),
                    ("sv", "El Salvador"),
                    ("sm", "San Marino"),
                    ("so", "Somalia"),
                    ("pm", "Saint Pierre and Miquelon"),
                    ("rs", "Serbia"),
                    ("ss", "South Sudan"),
                    ("st", "Sao Tome and Principe"),
                    ("sr", "Suriname"),
                    ("sk", "Slovakia"),
                    ("si", "Slovenia"),
                    ("se", "Sweden"),
                    ("sz", "Eswatini"),
                    ("sx", "Sint Maarten (Dutch part)"),
                    ("sc", "Seychelles"),
                    ("sy", "Syrian Arab Republic"),
                    ("tc", "Turks and Caicos Islands"),
                    ("td", "Chad"),
                    ("tg", "Togo"),
                    ("th", "Thailand"),
                    ("tj", "Tajikistan"),
                    ("tk", "Tokelau"),
                    ("tm", "Turkmenistan"),
                    ("tl", "Timor-Leste"),
                    ("to", "Tonga"),
                    ("tt", "Trinidad and Tobago"),
                    ("tn", "Tunisia"),
                    ("tr", "Turkey"),
                    ("tv", "Tuvalu"),
                    ("tw", "Taiwan, Province of China"),
                    ("tz", "Tanzania, United Republic of"),
                    ("ug", "Uganda"),
                    ("ua", "Ukraine"),
                    ("um", "United States Minor Outlying Islands"),
                    ("uy", "Uruguay"),
                    ("us", "United States"),
                    ("uz", "Uzbekistan"),
                    ("va", "Holy See (Vatican City State)"),
                    ("vc", "Saint Vincent and the Grenadines"),
                    ("ve", "Venezuela, Bolivarian Republic of"),
                    ("vg", "Virgin Islands, British"),
                    ("vi", "Virgin Islands, U.S."),
                    ("vn", "Viet Nam"),
                    ("vu", "Vanuatu"),
                    ("wf", "Wallis and Futuna"),
                    ("ws", "Samoa"),
                    ("ye", "Yemen"),
                    ("za", "South Africa"),
                    ("zm", "Zambia"),
                    ("zw", "Zimbabwe"),
                ],
                help_text="Select origin country of the request that this rule will match against. This rule will only work if you use Cloudflare or CloudFront IP geolocation or if GeoIP2 module is configured.",
                max_length=2,
            ),
        ),
    ]
