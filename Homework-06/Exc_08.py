def save_applicant_data(source, output):
    with open(output, 'w') as output_file:
        for dict in source:
            output_file.write(f"{dict['name']},{dict['specialty']},{dict['math']},{dict['lang']},{dict['eng']}\n")