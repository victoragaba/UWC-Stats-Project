co2025 = open("co2025.txt", mode="r", encoding="utf-8", errors="ignore")
my2025list = [line.strip() for line in co2025]
co2024 = open("co2024.txt", mode="r", encoding="utf-8", errors="ignore")
my2024list = [line.strip() for line in co2024]
T30 = open("T30.txt", mode="r", encoding="utf-8", errors="ignore")
myT30list = [line.strip() for line in T30]
# print(my2024list.index('Massachusetts Institute of'))
# print(myT30list)

ref_list = [
    'UWC Dilijan',
    'Waterford Kamhlaba UWC',
    'UWC Costa Rica',
    'UWC Robert Bosch College',
    'UWC in Mostar',
    'UWC Changshu China',
    'UWC ISAK Japan',
    'UWC South East Asia',
    'Pearson College UWC',
    'UWC Atlantic College',
    'UWC-USA',
    'UWC Red Cross Nordic',
    'UWC Maastricht',
    'UWC Mahindra College',
    'UWC Adriatic',
    'UWC Thailand',
    'Li Po Chun UWC',
    'UWC East Africa'
]

names25 = my2025list[::4]
names24 = my2024list[::4]
# print(names24[630:700])
# print(len(names24))
countries25 = my2025list[1::4]
countries24 = my2024list[1::4]
# print(countries)
# print([x for x in countries if "unknown" in x.lower()])
UWCs25 = my2025list[2::4]
UWCs24 = my2024list[2::4]
# print(UWCs24)

# new_list = [index*4 for index, element in enumerate(UWCs24) if element not in ref_list]
# print(new_list)

unis25 = my2025list[3::4]
unis24 = my2024list[3::4]
# print(unis)
# print([x for x in unis if "california" in x.lower()])

inner_peace = len(names25) == len(countries25) == len(UWCs25) == len(unis25)
# print(inner_peace)

# List of non-duplicated UWCs
myUWCs = []
for UWC in UWCs25:
    if UWC not in myUWCs:
        myUWCs.append(UWC)
# print(myUWCs)

def filter_category(category, query_elements):
    """
    Takes in two lists of strings
    """
    category_index = []
    def is_in_there(element, bunch):
        bool = False
        for query_element in bunch:
            if query_element.lower() in element.lower():
                bool = True
        return bool
            
    for index, element in enumerate(category):
        if is_in_there(element, query_elements):
            category_index.append(index)
    return category_index
# print(filter_category(UWCs25, "water"))

WKers = [names25[index] for index in filter_category(UWCs25, ["Waterford"])]
# print(len(WKers))
def see_WKers():
    for index in filter_category(UWCs25, ["Waterford"]):
        print(f"{names25[index]}: {unis25[index]}, {countries25[index]}\n")
# see_WKers()

def see_them(category, query_elements, year):
    def help(c1,c2,c3,c4):
        count = 0
        for index in filter_category(category, query_elements):
            print(f"{c1[index]}: {c2[index]}, {c3[index]}, {c4[index]}\n")
            count += 1
        return f"{count}/{len(c1)} ({round(count/len(c1)*100)}%)"

    if year == 2025:
        return help(names25, countries25, UWCs25, unis25)
    elif year == 2024:
        return help(names24, countries24, UWCs24, unis24)
# see_them(countries25, ["Uganda"], 2025)
# see_them(unis25, ["Oklahoma"], 2025)

"""
LINE OF INTEREST
"""
print(see_them(unis24, ["Northwestern"], 2024))

def see_T30(year):
    if year == 2025:
        T30 = filter_category(unis25, myT30list)
    elif year == 2024:
        T30 = filter_category(unis24, myT30list)

    def help(c1,c2,c3,c4):
        for index in T30:
            print(f"{c1[index]}: {c2[index]}, {c3[index]}, {c4[index]}\n")

    if year == 2025:
        help(names25,unis25,UWCs25,countries25)
    elif year == 2024:
        help(names24,unis24,UWCs24,countries24)
# see_T30(2025)

def banner(year):
    if year == 2025:
        yearnames = names25
        interest = len(filter_category(unis25, myT30list))
    elif year == 2024:
        yearnames = names24
        interest = len(filter_category(unis24, myT30list))
    print("-"*100 + f"\nThere are {interest} students out of {len(yearnames)} ({round(interest/len(yearnames)*100)}%)\n" + "-"*100 + "\n")

def by_school(year):
    popn = [0] * len(myUWCs)
    juice = [0] * len(myUWCs)
    
    if year == 2025:
        index = filter_category(unis25, myT30list)
        for datapoint in UWCs25:
            for num, UWC in enumerate(myUWCs):
                if datapoint == UWC:
                    popn[num] += 1
        for x in index:
            for num, UWC in enumerate(myUWCs):
                if UWCs25[x] == UWC:
                    juice[num] += 1

    elif year == 2024:
        index = filter_category(unis24, myT30list)
        for datapoint in UWCs24:
            for num, UWC in enumerate(myUWCs):
                if datapoint == UWC:
                    popn[num] += 1
        for x in index:
            for num, UWC in enumerate(myUWCs):
                if UWCs24[x] == UWC:
                    juice[num] += 1

    for num, UWC in enumerate(myUWCs):
        print(f"{UWC}: {juice[num]} in {popn[num]} ({round(juice[num]/popn[num]*100)}%)\n")
    # print(juice, sum(juice))

# while True:
#     haha = input("Year:")
#     banner(int(haha))
#     by_school(int(haha))

SEA25 = [f"{names25[x]}, {unis25[x]}" for x in filter_category(unis25, myT30list) if "south east asia" in UWCs25[x].lower()]
SEA24 = [f"{names24[x]}, {unis24[x]}" for x in filter_category(unis24, myT30list) if "south east asia" in UWCs24[x].lower()]
def see_SEA(year):
    if year == 2025:
        for x in SEA25:
            print(x + "\n")
    if year == 2024:
        for x in SEA24:
            print(x + "\n")
# see_SEA(2025)
SEA25_chic = [x for x in SEA25 if "chicago" in x.lower()]
SEA24_chic = [x for x in SEA24 if "chicago" in x.lower()]
# print("At UChicago:", len(SEA25_chic))