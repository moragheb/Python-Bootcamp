from mymodule import my_func
my_func()
from main_package.main_func import	main_func
main_func()
from main_package.Sub_main import sub_pack
sub_pack.sub_func()
print(__name__)

if __name__==__main__:
	