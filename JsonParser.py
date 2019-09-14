import json, os, sys

class JsonParser():

	""" Create or open a json and perform CRD """
	def __init__(self,json_path=None):
		
		self.json_path = json_path
		# Default path
		if self.json_path is None:
			print("\n","Created a file in current working directory File name : JsonDB.json")
			path = self.create_a_json_file(os.getcwd())
		# Opening an existing json file
		elif(self.json_path.endswith(".json")):
			print("\n","Editing a json file")
			path = self.json_path
		# Opening an empty folder
		else:
			path = self.create_a_json_file(self.json_path)
		self.perform_crd_on_json(path)

	def create_a_json_file(self,path):
		created_path = path+r"/JsonDB.json"
		f = open(created_path,"w+")
		f.close()
		return created_path

	def perform_crd_on_json(self,json_file):
		# Check its a empty file
		if (os.stat(json_file).st_size == 0):
			valid_json = self.get_a_valid_key_value_pair(json_file)	
			self.write_in_file(json_file,valid_json)
		else:
			# Create or delete operation
			self.update_the_json(json_file)
			
	def write_in_file(self,json_file,data):
		with open(json_file,"r+") as file:
			file.write(json.dumps(data))
		self.update_the_json(json_file)

	def update_the_json(self,json_file):
		
		option = self.get_an_input_option()

		# Core logic 
		if option == 1:
			# Adding a non existing key value pair
			incoming_data = self.get_a_valid_key_value_pair(json_file)
			existing_data = self.get_the_file_content_as_a_dict(json_file)
			incoming_data_key = list(incoming_data.keys())[0]
			its_okay = self.check_the_key_already_in_file(incoming_data_key,existing_data)
			
			if its_okay:
				self.clear_up_file_for_new_comers(json_file)
				existing_data.update(incoming_data)
				self.write_in_file(json_file,existing_data)
			else:
				print("\n")
				print("Oops that key already exist lets try again")
				self.update_the_json(json_file)

		elif option == 2:
			# print value by key if exist
			key = self.get_a_valid_key_value_pair(json_file,key_only=True)
			existing_data = self.get_the_file_content_as_a_dict(json_file)
			its_okay = self.check_the_key_already_in_file(key,existing_data)

			if not its_okay:
				print ("\n",json.dumps(existing_data[key],indent=4))
				self.update_the_json(json_file)
			else:
				print("\n","Key not found!")
				self.update_the_json(json_file)
		
		elif option == 3:
			# deletion 
			key = self.get_a_valid_key_value_pair(json_file,key_only=True)
			existing_data = self.get_the_file_content_as_a_dict(json_file)
			its_okay = self.check_the_key_already_in_file(key,existing_data)
			if not its_okay:
				self.clear_up_file_for_new_comers(json_file)
				deleted = existing_data[key]
				del[existing_data[key]]
				print("\n","Deleted successfully!")
				self.write_in_file(json_file,existing_data)
				self.update_the_json(json_file)
			else:
				print("\n","Key not found!")
				self.update_the_json(json_file)


		elif option == 4:
			# Pretty printing the current structure
			data = self.get_the_file_content_as_a_dict(json_file)
			print("\n",json.dumps(data,indent=4))
			self.update_the_json(json_file)

		elif option == 5:
			sys.exit()

		else:
			print("Please choose a valid option")
			self.update_the_json(json_file)

	def get_the_file_content_as_a_dict(self,json_file):
		with open(json_file,"r") as file:
			return json.load(file)

	def clear_up_file_for_new_comers(self,json_file):
		with open(json_file,"w") as file:
			file.truncate(0)

	def get_a_valid_key_value_pair(self,json_file,key_only=None):
		try:
			key = input("Enter key : ")
			if key_only is not None:
				return key
			data = {}
			# Value is always a json object
			value = eval(str(input("Enter the value as json object : ")).replace("\"","'"))
			if(isinstance(value,dict)):
				data[key]=value
				return data
			else:
				print("Enter a valid JSON ")
				JsonParser(json_file)
		except:
			print("Enter a valid JSON ")
			JsonParser(json_file)
	
	def check_the_key_already_in_file(self,incoming_data_key,existing_data):
		if incoming_data_key in existing_data.keys():
			return False
		return True

	def get_an_input_option(self):
		inputs = [1,2,3,4,5]
		print("\n")
		print(f"Choose Something intresting \n=========================== \n {inputs[0]} => Add a new key value \n {inputs[1]} => Read value by key \n {inputs[2]} => Delete by key \n {inputs[3]} => View the whole structure")
		user_input = eval(input(" 5 => Exit : "))
		if isinstance(user_input,int) and user_input in inputs:
			return user_input
		else:
			print("Please Choose a valid option")
			return None




if __name__ == "__main__":
	
	if(len(sys.argv) == 2):
		if(os.path.exists(sys.argv[-1])):
			JsonParser(sys.argv[-1])
		else:
			print("Please enter a valid path")
			sys.exit()
	JsonParser()