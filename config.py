#
# Reads from MDroid configuration file, used across several Python scripts
# in the MDroid suite.
#
import argparse
import os
import json
import logging

# Parse through a json file containing a 2D array
# Each of the searchValues requested are required, 
# we will return all or None.
def _parseConfigFile(configFile, searchValues: dict) -> dict:
	returnDict = dict()

	for key in searchValues.keys():
		if key in configFile:
			# Make sure this parent key is in our return
			if key not in returnDict:
				returnDict[key] = dict()

			# Parse through each child value 
			for value in searchValues[key]:
				# Add child value to return, if it exists
				if value in configFile[key]:
					returnDict[key][value] = configFile[key][value]
				else:
					# Value not found, return none
					logging.error(value+" not found in config file.")
					return None
		else:
			# Key not found, return none
			logging.error("Settings file does not contain key "+str(key))
			return None
	return returnDict

# Given filename and dict of values to find,
# return a dict with the same formatting
def readConfig(values: dict) -> dict:
	# parse program arguments
	parser = argparse.ArgumentParser(description='Read from GPSd, forward to REST API.')
	parser.add_argument('--settings-file', action='store', required=True, help='Config file to load API settings.')
	args = parser.parse_args()

	if args and args.settings_file:
		if os.path.isfile(args.settings_file): 
			try:
				with open(args.settings_file) as json_file:
					configData = json.load(json_file)
					return _parseConfigFile(configData, values)
			except IOError as e:
				logging.error("Failed to open settings file:"+args.settings_file)
				logging.error(e)
				return None
		else:
			logging.error("Could not load settings from file"+str(args.settings_file))
			return None
	return False

# Run some quick tests
if __name__ == "__main__":
	testJson = json.loads('{"MDROID": {"TEST_SETTING": 123, "TEST_SETTING2": "ABC", "TEST_SETTING3": "NOT"}, "Not Retrieved": "Sure.", "Again Not, but with children": {"Even": "Better"}}')

	testDict1 = {
		"MDROID": {
			"TEST_SETTING",
			"TEST_SETTING2"
		}
	}
	testDict2 = {
		"MDROID": {
			"TEST_SETTING",
			"UNKNOWN_SETTING"
		}
	}
	expectedDict1 = {
		"MDROID": {
			"TEST_SETTING": 123,
			"TEST_SETTING2": "ABC"
		}
	}

	# Test
	print("Testing first dict...")
	test1 = _parseConfigFile(testJson, testDict1)
	print(test1)
	assert(test1 == expectedDict1)
	print("OK")
	print("Testing second dict...")
	assert(_parseConfigFile(testJson, testDict2) == None)
	print("OK")