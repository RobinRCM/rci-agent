from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
import torch
import time


### TRY WITH LLAMA CPP BY GGML

# tokenizer = AutoTokenizer.from_pretrained("TheBloke/Llama-2-7b-Chat-GPTQ")
# model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7b-Chat-GPTQ")
def llama2_7b_chat_gptq():
    from transformers import pipeline, logging
    from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

    model_name_or_path = "TheBloke/Llama-2-7b-Chat-GPTQ"
    model_basename = "gptq_model-4bit-128g"

    use_triton = False

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

    model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
            model_basename=model_basename,
            use_safetensors=True,
            trust_remote_code=True,
            device="mps",
            use_triton=use_triton,
            quantize_config=None)


def llama_2_ggml_7b_chat():
    model = AutoModel.from_pretrained("TheBloke/Llama-2-7B-Chat-GGML")

def stable_beluga_inference():

    tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga-7B")
    model = AutoModelForCausalLM.from_pretrained("stabilityai/StableBeluga-7B")

    # print(model)

    mps = torch.device("mps")
    print(mps)

    input_text = "How much is 12 + 10?"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    input_ids.to(mps)

    print(f"INPUT IDS: {input_ids}\n")

    output = model.generate(input_ids, max_length=50, temperature=1.0)

    print(f"OUTPUT: {output}\n")

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)

def mpt_7b_instruct():
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
    model = AutoModelForCausalLM.from_pretrained('mosaicml/mpt-7b-instruct', trust_remote_code=True)
    input_text = "<human>: How much is 12 + 10?\n<bot>:" #"<human>: Who is Alan Turing?\n<bot>:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # print(f"INPUT IDS: {input_ids}\n")
    # model = model.to('mps')
    # input_ids = input_ids.to('mps')

    # start = time.time()
    # output = model.generate(input_ids, pad_token_id=tokenizer.eos_token_id, max_length=50, temperature=1.0)
    output = model.generate(input_ids, max_length=50, temperature=1.0)
    # end = time.time() - start
    # print(f"Took {end} seconds\n")
    # print(f"OUTPUT: {output}\n")
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)


def red_pajama_chat_3b(input_text):
    tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1")
    red_pajama = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1")

    # print(f"RED PAJAMA: {red_pajama}\n")

    # mps = torch.device("mps")
    # print(mps)

    # input_text = "<human>: How much is 12 + 10?\n<bot>:" #"<human>: Who is Alan Turing?\n<bot>:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # print(f"INPUT IDS: {input_ids}\n")
    #red_pajama = red_pajama.to('mps')
    #input_ids = input_ids.to('mps')

    start = time.time()
    output = red_pajama.generate(input_ids, pad_token_id=tokenizer.eos_token_id, max_new_tokens=200, temperature=1.0)
    end = time.time() - start
    print(f"Took {end} seconds\n")

    # print(f"OUTPUT: {output}\n")

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)





#instruction = "<human>: How much is 12 + 10?\n<bot>:"

webpage_extract = """
                    <div>
                        <div>
                        <div>
                        <div>
                        <div>
                            <div>
                            <img alt="S3" height="24" src="https://d2ftaif6zn7k3h.cloudfront.net/icon/c0828e0381730befd1f7a025057c74fb-43acc0496e64afba82dbc9ab774dc622.svg" width="24"/>
                            <div class="linkWrapper-0-1-98">
                            <a data-testid="recently-visited-link-s3" href="https://s3.console.aws.amazon.com/s3/home?region=eu-west-3">
                            S3
                            </a>
                            </div>
                            </div>
                        </div>
                        <div data-testid="recently-visited-ec2">
                            <div>
                            <img alt="EC2" height="24" src="https://d2ftaif6zn7k3h.cloudfront.net/icon/d88319dfa5d204f019b4284149886c59-7d586ea82f792b61a8c87de60565133d.svg" width="24"/>
                            <div>
                            <a data-analytics="serviceLink_ec2" data-analytics-funnel-value="link:r7r:" data-analytics-type="eventDetail" data-testid="recently-visited-link-ec2" href="https://eu-west-3.console.aws.amazon.com/ec2/home?region=eu-west-3" id="link-self:r7s:">
                            EC2
                            </a>
                            </div>
                            </div>
                        </div>

                       <div>
                        <button aria-label='Add "S3" to favorites' data-testid="service-list-item-toggle-favorite-button-s3" type="button">
                        </button>
                        <a data-testid="s3" href="https://s3.console.aws.amazon.com/s3/home?region=eu-west-3" role="link" target="_top" title="Scalable Storage in the Cloud">
                         <h4>
                          S3
                         </h4>
                         <p>
                          Scalable Storage in the Cloud
                         </p>
                        </a>
                       </div>
                      </li>
                      <li data-testid="-ec2">
                       <div>
                        <button aria-label='Add "EC2" to favorites' data-testid="service-list-item-toggle-favorite-button-ec2" type="button">
                        </button>
                        <a data-testid="ec2" href="https://eu-west-3.console.aws.amazon.com/ec2/home?region=eu-west-3" role="link" target="_top" title="Virtual Servers in the Cloud">
                         <h4>
                          EC2
                         </h4>
                         <p>
                          Virtual Servers in the Cloud
                         </p>
                        </a>
                       </div>
"""

instruction = "<human>:" + \
"""You are an autonomous web navigation agent.
You are given this webpage. What are the possible actions the user can do?
Describe all the possible actions on this page.\n\n""" + webpage_extract \
+ "\n<bot>:"

# instruction = "<human>:" + \
# """You are an autonomous web navigation agent.

# Your possible actions are:
# - `clickxpath /path/to/the/element`
# - `type input`

# You are given this webpage. What are the possible actions the user can do? a user has to create an S3 bucket. What should the action be ?
# The action should follow the regex pattern:
# - '^clickxpath\s//\S+$' if this is a click action
# - '^type\s[^"]{1,}$' if this is a type action

# <div>
# <button aria-label='Add "EC2" to favorites' data-testid="service-list-item-toggle-favorite-button-ec2" type="button">
# </button>
# <a data-testid="ec2" href="https://eu-west-3.console.aws.amazon.com/ec2/home?region=eu-west-3" role="link" target="_top" title="Virtual Servers in the Cloud">
#     <h4>
#     EC2
#     </h4>
#     <p>
#     Virtual Servers in the Cloud
#     </p>
# </a>
# </div>""" \
# + "\n<bot>:"

# red_pajama_chat_3b(instruction)


llama_2_ggml_7b_chat()



# mpt_7b_instruct()

    # model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b", trust_remote_code=True)
    # model

    # print(model)

# stable_beluga_inference()

# # PROMPT FORMAT

# ### System:
# This is a system prompt, please behave and help the user.

# ### User:
# Your prompt here

# ### Assistant:
# The output of Stable Beluga 7B


# from transformers import AutoTokenizer, AutoModelForCausalLM
# import transformers
# import torch

# #model = "tiiuae/falcon-7b"
# model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b", trust_remote_code=True)

# tokenizer = AutoTokenizer.from_pretrained(model)
# pipeline = transformers.pipeline(
#     "text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     torch_dtype=torch.bfloat16,
#     trust_remote_code=True,
#     device_map="auto",
# )
# sequences = pipeline(
#    "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
#     max_length=200,
#     do_sample=True,
#     top_k=10,
#     num_return_sequences=1,
#     eos_token_id=tokenizer.eos_token_id,
# )
# for seq in sequences:
#     print(f"Result: {seq['generated_text']}")
