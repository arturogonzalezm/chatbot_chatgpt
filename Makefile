update_env:
	@echo "Updating the 'chatbot_chatgpt' Conda environment from environment.yml..."
	conda env update --name chatbot_chatgpt --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate chatbot_chatgpt"
