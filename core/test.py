



# USER=(
# 	request_to_create_a_new_community -> 
# 	display_community_form -> 
# 	submit_information -> 
# 	(
# 	tagname_count_is_zerro-> redirect_to_community_page ->USER 
# 	|
# 	tagname_count_is_not_zerro-> error_message -> USER
# 	)
# 	).


# EWU_CONNECT=(


# 	request_to_create_a_new_community -> 
# 	display_community_form -> submit_information -> 
# 	generateCommunityTagname -> 
# 	getTagNameList_counter ->
# 	totalList_counter->
# 	(tagname_count_is_not_zerro-> error_message -> EWU_CONNECT
# 	|tagname_count_is_zerro-> queryInformation -> ok -> redirect_to_community_page ->EWU_CONNECT
# 	)
	
# 	).

# DATABASE=(

# 	getTagNameList_counter ->

# 	totalList_counter->
#     (tagname_count_is_zerro ->
#         queryInformation -> ok ->DATABASE 
#     | STOP
# 	)

# ).

# ||CREATE=(USER||EWU_CONNECT||DATABASE).






