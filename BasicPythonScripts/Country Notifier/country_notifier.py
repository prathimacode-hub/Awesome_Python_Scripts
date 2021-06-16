from countryinfo import CountryInfo

#country name for which detail is needed
country_name="India"
a= CountryInfo(country_name)

info_1=a.alt_spellings()
print(info_1)

#finding capital
info_2= a.capital()
print(info_2)

#languages
info_3= a.languages()
print(info_3)

#time zone of country
info_4=a.timezones()
print(info_4)

#currency of country
info_5=a.currencies()
print(info_5)

#area of country
info_6=a.area()
print(info_6)


info_7=a.borders()
print(info_7)

#country code foe calling
info_8=a.calling_codes()
print(info_8)

#wikipedia link of country
info_9= a.wiki()
print(info_9)

info_10=a.info()
for p,q in info_10.items():
    print(f'{p}     {q}')