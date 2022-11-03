from models.person import Person

prs1 = Person.create_from_json_file("sample_person.json")
prs2 = Person.create_from_json_file("other_person.json")
mprs = Person.create_from_json_file("many_persons.json")

Person.write_to_json_file("new_file.json", mprs)

