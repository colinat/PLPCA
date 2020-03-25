## intent:greet
- Hello
- hey
- good evening
- Hi
- good morning
- hi again
- hey there
- hello

## intent:goodbye
- gotta go
- cya
- good bye
- good night
- goodbye
- see you around
- see you later
- goodnight
- bye

## intent:thanks
- Thank you so much
- Thanks
- Thanks for that
- Thank you
- Thank u

## intent:ask_what_can_u_do
- help me
- What can you do
- What can you do?
- what do u do?
- How are you able to help me
- what can u do

## intent:inform
- [earnings](aspect_type)
- [products_services](aspect_type)
- [op_costs](aspect_type)
- [debt](aspect_type)
- [organic_expansion](aspect_type)
- [acquisitions](aspect_type)
- [sales](aspect_type)

## intent:query_sentiment
- Is management [optimistic](emot_polarity)?
- Have interest rate trends benefited/acted against the company?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- Can we expect to see accelerating return from the investments?
- Should we expect to see a net impact in [sales](aspect_type)?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- How have our [acquisitions](aspect_type) performed?
- How far can [stock price](aspect_type:earnings) go this year?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- So should we expect a reversal or a benefit in the fourth quarter?
- Is there expectation for growth to moderate?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- What is the general [tone](emot_polarity) of management?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- How should we see any impacts on [revenue](aspect_type:sales)?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- How is the company's balance sheet and [debt](aspect_type) level?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- What is the overall [outlook](sent_polarity) for the company as a whole?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- Will I [make money](sent_polarity) from this stock this year?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- How is the company performing vs our [competitors](aspect_type:competition)?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?

## intent:query_sentence
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- Why have [sales](aspect_type) not been up to expectations?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Are [earnings](aspect_type) performing in line with expectations?
- What's driving the more optimistic expectation for [sales](aspect_type)?
- What caused margin [to decline](sent_polarity:negative)?
- What is holding back the [sales](aspect_type) growth this quarter?
- Any changes in the [sales](aspect_type) trends?

## intent:out_of_scope
- are you russian?
- I want to order pizza
- I already told you! I'm a shitmuncher
- I changed my mind
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- are you vegan
- NLW
- are you sick
- buy groceries
- Who’s the US President?
- are you using Rasa Core and NLU ?
- What day is it today?
- Do I have to accept?
- Today
- What is your hobbies?
- I want pizza
- Can you give me your datacenter's password
- I am User
- chinese ok?
- Can YouTube talk?
- I wan to buy a plane
- Can I ask you questions first?
- Where am I right now?
- What did you eat yesterday?
- can you book dinner
- Can I get a hamburger?
- Why don’t you answer?
- I'm a shitmuncher
- I want a new laptop
- What is 2 + 2?
- I can barely see this white text on light gray background ...
- What's do YouTube do
- Is today saturday?
- I am asking you an out of scope question
- but if rasa is open source why do you have a sales team
- cr
- Try it out broken
- Find nearest pizzahut
- aRE YOU SINGLE
- book a ticket
- I want book a hotel
- but I just told you that :(
- Make me a sandwich
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- can you cook dinner
- german?
- chgfhgh
- can you give me a cup of coffee
- cannot see
- What is todays date
- What's your backend system?
- common, just try
- I want to die
- Is this Goal-Oriented Chatbot?
- What do you prefer?
- Can you call me back ?
- I wanna marry you
- I want to order food
- can you cheer me up
- I am an opioid addic
- What makes you better than a human?
- buy one please
- I want french cuisine
- But you're an english site :(
- Won't you ask me how I am?
- can you help me with your docs?
- Why is my TRUST score set to 50 after I completed the registration process?
- Nice name
- I want to use pipe
- can we keep chatting?
- Who ?
- Mail me the guide
- I have installed it
- Can you please send me an uber
- are you human ?
- The Try it out is not working
- I need a job
- are u facebook
- Kristin, I want to marry you
- I am hungry
- are you single?
- I ned a GP in 94301
- colder
- Now?
- Can you give me your datacenter's password?
- Order me a pizza
- can you learn from our conversation?
- You'r blue.
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- Have we met before?
- Recharge
- Are you ready?
- connect to alexa
- are u, facebook?
- alexa, order 5 tons of natrium chloride
- again?

## synonym:acquisitions
- aquisition
- acquisituoin
- buyout
- M&A
- mergers

## synonym:competition
- competitors
- competitive landscape
- challengers

## synonym:confident
- optimistic

## synonym:debt
- gearing
- leverage
- geared
- liquidity
- financing
- loan
- loans

## synonym:earnings
- margins
- profit margin
- stock price
- performance
- bottom line
- net profit
- bottomline
- eps
- EPS
- result
- net margin
- net margins

## synonym:negative
- to decline
- rising costs

## synonym:op_costs
- operating costs
- costs
- expenses
- gross margin
- gross margins
- cost
- overheads
- opex
- operational cost
- operation cost
- operating cost
- operational expense
- operation expense

## synonym:op_risks
- risks
- challenges
- business risks
- operational risk
- operation risk
- operating risk
- ops risks

## synonym:organic_expansion
- expansion
- expansion plans
- growth strategy

## synonym:products_services
- products
- business
- business division
- biz

## synonym:sales
- revenue
- sales
- net revenue
- topline
