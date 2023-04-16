from utilities import read_utils

test_invalid_login_data=[
    ("einfochips", "Invalid credentials"), ("einfochips123", "Invalid credentials")

]


test_valid_login=[
    ("test","test1","test@test.com","engineer","einfochips","9999999999","301-500","India"),
    ("test1", "test2", "test123@test.com", "engineer11", "einfochips123", "9999999900", "301-500", "India")
]


test_invalid_login=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")

test_add_valid_data=read_utils.get_csv_as_list("../test_data/test_valid_login_hr.xlsx")