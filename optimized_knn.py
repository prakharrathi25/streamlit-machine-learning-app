result_forms = []
	result_cookies = []
	result = []
	if tc_flag == 1:
		text = terms_parser(url)
		result = search_text(str(text))
	else:
		if c_status!=-1:
			cookies = json.loads(cookies)
			cleaned_cookies = [clean(cookie) for cookie in cookies.keys()]
			all_cookies = " ".join([c for c in cleaned_cookies])
		else:
			all_cookies = ""

		if f_status!=-1:
			all_forms = str(list_of_forms)
		else:
			all_forms = ""

		all_info = all_forms + all_cookies

		result_forms = search_text(all_forms)
		result_cookies = search_text(all_cookies)
		result = search_text(all_info)

	result = list(set(result))
	for record in result:
		if record in personal_dict.keys():
			personal_dict[record] = 1
		elif record in sensitive_personal_dict.keys():
			sensitive_personal_dict[record] = 1


	spi = sensitive_personal_dict.copy()
	pi = personal_dict.copy()
	result_dict = merge_dictionary(pi,spi)

	print(result_dict)
