from pymongo.mongo_client import MongoClient

# MongoDB URI
URI = "mongodb+srv://VenkatSagi:mongodb.2004@cluster0.ijkgw8w.mongodb.net/?retryWrites=true&w=majority"

# Variables for Client, Database, Collection
client = MongoClient(URI)
dataBase = client['ToyotaRaces']
collection = dataBase['DragStripRaces']

# Variable to store Race Data
dsRaceData = [
    {
        "Date": "01-06-2023",
        "Time": "06:00 AM - 06:01 AM",
        "Vehicle": "Toyota GR Supra",
        "Location of Race": "Santa Pod Raceway",
        "Total Race Time": "00:09:870",
        "Reaction Time": "00:00:500",
        "60-foot time": "00:01:500",
        "330-foot time": "00:04:000",
        "660-foot time": "00:06:000",
        "1/8-mile speed": "90 mph",
        "1,000-foot time": "00:07:800",
        "1/4-mile time": "00:09:870",
        "1/4-mile speed": "135 mph",
        "MPH": "145"
    },
    {
        "Date": "02-06-2023",
        "Time": "07:00 AM - 07:01 AM",
        "Vehicle": "Toyota GR Yaris",
        "Location of Race": "York Raceway",
        "Total Race Time": "00:10:250",
        "Reaction Time": "00:00:600",
        "60-foot time": "00:01:600",
        "330-foot time": "00:04:100",
        "660-foot time": "00:06:100",
        "1/8-mile speed": "85 mph",
        "1,000-foot time": "00:08:200",
        "1/4-mile time": "00:10:250",
        "1/4-mile speed": "130 mph",
        "MPH": "140"
    },
    {
        "Date": "03-06-2023",
        "Time": "08:00 AM - 08:01 AM",
        "Vehicle": "Toyota 86",
        "Location of Race": "Shakespeare County Raceway",
        "Total Race Time": "00:11:120",
        "Reaction Time": "00:00:700",
        "60-foot time": "00:01:700",
        "330-foot time": "00:04:200",
        "660-foot time": "00:06:200",
        "1/8-mile speed": "80 mph",
        "1,000-foot time": "00:08:600",
        "1/4-mile time": "00:11:120",
        "1/4-mile speed": "125 mph",
        "MPH": "135"
    },
    {
        "Date": "04-06-2023",
        "Time": "09:00 AM - 09:01 AM",
        "Vehicle": "Toyota C-HR GR Sport",
        "Location of Race": "Elvington Airfield",
        "Total Race Time": "00:12:450",
        "Reaction Time": "00:00:800",
        "60-foot time": "00:01:800",
        "330-foot time": "00:04:300",
        "660-foot time": "00:06:300",
        "1/8-mile speed": "75 mph",
        "1,000-foot time": "00:09:000",
        "1/4-mile time": "00:12:450",
        "1/4-mile speed": "120 mph",
        "MPH": "130"
    },
    {
        "Date": "05-06-2023",
        "Time": "10:00 AM - 10:01 AM",
        "Vehicle": "Toyota Land Cruiser",
        "Location of Race": "North Weald Airfield",
        "Total Race Time": "00:13:300",
        "Reaction Time": "00:00:900",
        "60-foot time": "00:01:900",
        "330-foot time": "00:04:400",
        "660-foot time": "00:06:400",
        "1/8-mile speed": "70 mph",
        "1,000-foot time": "00:09:400",
        "1/4-mile time": "00:13:300",
        "1/4-mile speed": "115 mph",
        "MPH": "125"
    },
    {
        "Date": "06-06-2023",
        "Time": "11:00 AM - 11:01 AM",
        "Vehicle": "Toyota Hilux",
        "Location of Race": "Dunsfold Aerodrome",
        "Total Race Time": "00:14:200",
        "Reaction Time": "00:01:000",
        "60-foot time": "00:02:000",
        "330-foot time": "00:04:500",
        "660-foot time": "00:06:500",
        "1/8-mile speed": "65 mph",
        "1,000-foot time": "00:09:800",
        "1/4-mile time": "00:14:200",
        "1/4-mile speed": "110 mph",
        "MPH": "120"
    },
    {
        "Date": "07-06-2023",
        "Time": "12:00 PM - 12:01 PM",
        "Vehicle": "Toyota Proace City",
        "Location of Race": "Bruntingthorpe Proving Ground",
        "Total Race Time": "00:15:100",
        "Reaction Time": "00:01:100",
        "60-foot time": "00:02:100",
        "330-foot time": "00:04:600",
        "660-foot time": "00:06:600",
        "1/8-mile speed": "60 mph",
        "1,000-foot time": "00:10:200",
        "1/4-mile time": "00:15:100",
        "1/4-mile speed": "105 mph",
        "MPH": "115"
    },
    {
        "Date": "08-06-2023",
        "Time": "01:00 PM - 01:01 PM",
        "Vehicle": "Toyota Aygo X Prologue",
        "Location of Race": "Millbrook Proving Ground",
        "Total Race Time": "00:16:000",
        "Reaction Time": "00:01:200",
        "60-foot time": "00:02:200",
        "330-foot time": "00:04:700",
        "660-foot time": "00:06:700",
        "1/8-mile speed": "55 mph",
        "1,000-foot time": "00:10:600",
        "1/4-mile time": "00:16:000",
        "1/4-mile speed": "100 mph",
        "MPH": "110"
    },
    {
        "Date": "09-06-2023",
        "Time": "02:00 PM - 02:01 PM",
        "Vehicle": "Toyota Mirai",
        "Location of Race": "Longcross Test Track",
        "Total Race Time": "00:16:900",
        "Reaction Time": "00:01:300",
        "60-foot time": "00:02:300",
        "330-foot time": "00:04:800",
        "660-foot time": "00:06:800",
        "1/8-mile speed": "50 mph",
        "1,000-foot time": "00:11:000",
        "1/4-mile time": "00:16:900",
        "1/4-mile speed": "95 mph",
        "MPH": "105"
    },
    {
        "Date": "10-06-2023",
        "Time": "03:00 PM - 03:01 PM",
        "Vehicle": "Toyota Prius Plug-in Hybrid",
        "Location of Race": "Rockingham Motor Speedway",
        "Total Race Time": "00:17:800",
        "Reaction Time": "00:01:400",
        "60-foot time": "00:02:400",
        "330-foot time": "00:04:900",
        "660-foot time": "00:06:900",
        "1/8-mile speed": "45 mph",
        "1,000-foot time": "00:11:400",
        "1/4-mile time": "00:17:800",
        "1/4-mile speed": "90 mph",
        "MPH": "100"
    }

]


# Insert dsRaceData
collection.insert_many(dsRaceData)

print("FINISHED!!!")