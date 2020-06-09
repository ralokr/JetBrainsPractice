monthConversions = {
	
	"Jan" : "January",
	"Feb" : "February",
	"Mar" : "March",
	"Apr" : "April",
	"May" : "May",
	"Jun" : "June",
	"Jul" : "July",
	"Aug" : "August",
	"Sep" : "September",
	"Oct" : "October",
	"Nov" : "November",
	"Dec" : "December",
}



print(monthConversions["Feb"])

# OR

print(monthConversions.get("June","Invalid Key"))	#lets you specify a default value in case the key is not found