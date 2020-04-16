import json


class Response:
    def __init__(self, field_names, data):
        self.field_names = field_names
        self.data = data

    def get_response_json(self):
        """
        Return the processed JSON to be passed to the user
        :return:
        """
        tagged_data = self._add_db_field_names()
        return_json = self._build_json_response(tagged_data)

        return json.dumps(return_json)

    def _build_json_response(self, tagged_data):
        """
        Build the json structure to return to clients
        Assemble the general metadata section of the response combined with provided data
        :param data:
        :return:
        """
        output_data_structure = {'meta': self._create_metadata(), 'data': tagged_data}

        return output_data_structure

    @staticmethod
    def _create_metadata():
        """
        Create metadata section to be appended into the response form the server
        :return:
        """
        metadata = {"apiVersion": "v1", "request_timestamp": "now!"}

        return metadata

    def _add_db_field_names(self):
        """
        Will loop through the data supplied and append the appropriate field name
        :param field_names:
        :param data: list of lists (database records)
        :return: list of dicts (dict[field_name] = data)
        """
        fixed = []
        # Add field names to data
        # Take list of lists, make list of dicts

        # Loop through each record returned
        for single_record in self.data:
            row = {}
            # Loop through each field to append field name
            for index, elem in enumerate(single_record):
                row[self.field_names[index]] = elem

            fixed.append(row)

        return fixed
