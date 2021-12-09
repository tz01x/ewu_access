



# USER=(
# 	request_to_create_a_new_community -> 
# 	display_community_form -> 
# 	submit_information -> 
# 	(
# 	 redirect_to_community_page ->USER 
# 	|
# 	 error_message -> USER
# 	)
# 	).


# EWU_CONNECT=(


# 	request_to_create_a_new_community -> 
# 	display_community_form -> submit_information -> 
# 	generateCommunityTagname -> 
# 	request_for_new_community ->
# 	(
# 	success->
# 	redirect_to_community_page ->EWU_CONNECT
# 	|
# 	faild -> error_message -> EWU_CONNECT
# 	)
	
	
# 	).

# DATABASE=(

# 	request_for_new_community -> check_if_tag_is_unique->
# 	 (success -> DATABASE | faild -> DATABASE )

# ).

# ||CREATE=(USER||EWU_CONNECT||DATABASE).






