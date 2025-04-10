from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
def generate_retuarent_name_and_menu(cuisine):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.7)
    prompt = PromptTemplate(input_variables=['cuisine'],
                            template="I want to opne a restaurent for {cuisine} food. Suggest me a fancy name for it. output should be only 1 name. No explanation.")
    Name_chain = LLMChain(llm=llm, prompt=prompt,output_key='restaurent_name')
    prompt = PromptTemplate(input_variables=['restaurent_name'],
                            template="Suggest me some menutems for {cuisine} food. Return it as a comma seperated list.")
    Menu_chain = LLMChain(llm=llm, prompt=prompt, output_key='menu_items')
    chain= SequentialChain(
        chains=[Name_chain, Menu_chain],
        input_variables=['cuisine'],
        output_variables=['restaurent_name','menu_items']
        )
    result = chain.invoke({'cuisine': cuisine})
    return result  
if __name__=="__main__":
    print(generate_retuarent_name_and_menu('Italian'))