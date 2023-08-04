# from transformers import AutoProcessor, MarkupLMForPretraining

# processor = AutoProcessor.from_pretrained("microsoft/markuplm-base")
# model = MarkupLMForPretraining.from_pretrained("microsoft/markuplm-base")

from transformers import MarkupLMProcessor, MarkupLMForQuestionAnswering

processor = MarkupLMProcessor.from_pretrained("microsoft/markuplm-base-finetuned-websrc")
model = MarkupLMForQuestionAnswering.from_pretrained("microsoft/markuplm-base-finetuned-websrc")

# from load_falcon_7b import webpage_extract
\
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

question = "what are the potential services?"

encoding = processor(webpage_extract, questions=question, return_tensors="pt")

for k,v in encoding.items():
  print(k,v.shape)


import torch

# we use torch.no_grad() as we don't need any gradient computation here
# we're just doing inference! This saves memory
with torch.no_grad():
  outputs = model(**encoding)
  print(f"OUTPUTS: {outputs}\n")

answer_start_index = outputs.start_logits.argmax()
answer_end_index = outputs.end_logits.argmax()

predict_answer_tokens = encoding.input_ids[0, answer_start_index : answer_end_index + 1]
answer_string = processor.decode(predict_answer_tokens, skip_special_tokens=True)

print(f"ANSWER: {answer_string}\n")
