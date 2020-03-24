## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi
- Hey
- Hello
- hi again

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- goodnight
- good bye
- good night
- see ya
- cya
- bye bye
- gotta go
- farewell

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thank u
- Thanks for that
- thanks
- thnaks

## intent:ask_what_can_u_do
- What can you do?
- How can you help me?
- What can you do
- How are you able to help me
- what do u do?
- what can u do
- help
- help me

## intent:inform
- [sales](aspect_type)
- [earnings](aspect_type)
- [op_costs](aspect_type)
- [products_services](aspect_type)
- [organic_expansion](aspect_type)
- [acquisitions](aspect_type)
- [competition](aspect_type)
- [op_risks](aspect_type)
- [debt](aspect_type)

## intent:query_sentiment
- Should we expect to see a net impact in [sales](aspect_type)?
- How should we see any impacts on [revenue](aspect_type:sales)?
- Would the CEO expect the [negative](sent_polarity:negative) trend to reverse?
- So should we expect a reversal or a benefit in the fourth quarter?
- Is there expectation for growth to moderate? 
- Will growth rate be expected to reaccelerate from here?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- How are company's [expenses](aspect_type:op_costs) trending?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- How have our [acquisitions](aspect_type) performed?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Can we expect to see accelerating return from the investments?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Is company expected to be active on the merger and acquistion front this year?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year? 
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown 
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- How is the company's balance sheet and [debt](aspect_type) level?
- Have interest rate trends benefited/acted against the company?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- What is the general [tone](emot_polarity) of management?
- Is management [optimistic](emot_polarity)?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- What is the [outlook](sent_polarity) for share price of the company?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- How far can [stock price](aspect_type:earnings) go this year?
- Will I [make money](sent_polarity) from this stock this year?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?


## intent:query_sentence
- What are the primary drivers of [sales](aspect_type)?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- Are [earnings](aspect_type) performing in line with expectations? 
- Why have [sales](aspect_type) not been up to expectations?
- What caused margin [to decline](sent_polarity:negative)?
- Should we expect to see a net impact in margin?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What's driving the more optimistic expectation for [sales](aspect_type)? 
- What is holding back the [sales](aspect_type) growth this quarter?
- Any changes in the [sales](aspect_type) trends?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- What are some management comments on the [bullish](emot_polarity:confident) [earnings](aspect_type:earnings) [outlook](sent_polarity)?
- Can you elaborate on the reasons behind management's [optimism](emot_polarity:confident)?
- What is CEO's thoughts on our [competitors](aspect_type:competition)?
- Can you explain why CEO is [bearish](emot_polarity:negative) on [sales](aspect_type:sales) and outlook of the company?
- What are the reasons behind the forecast for [rising costs](sent_polarity:negative)?
- Why is the CEO [upbeat](sent_polarity:positve) on [earnings](aspect_type:earnings)?
- I wish to know what CEO said about our company outlook for [earnings](aspect_type:earnings)?
- Any explanation for the [exciting](sent_polarity:positive) outlook?
- Why is sentiment for [operating costs](aspect_type:op_costs) so [negative](sent_polarity)?
- Can you tell me why CEO is so [upbeat](sent_polarity:positve) on upcoming performance?
- Any comments on possible [acquisitions](aspect_type:acquisitions)?
- Any outlook on where our biggest [costs](aspect_type:op_costs) are going to trend?
- Why is it that management is [bullish](emot_polarity) on [earnings](aspect_type:earnings)?
- What are some driving factors behind managements [positive opinion](sent_polarity) on [earnings](aspect_type:earnings)?
- What is management saying about our [competitors](aspect_type:competition)?
- What are key things management highlighted about our [borrowings](aspect_type:debt) and [interest costs](aspect_type:debt)?
- What are important areas CEO highlighted about our key [competitors](aspect_type:competition)?
- What did CEO say about upcoming [earnings](aspect_type:earnings) forecast?
- What are some of CEO's views on potential [market share](aspect_type:organic_expansion) increase?
- Why is outlook for [earnings](aspect_type:earnings) so [bad](sent_polarity:negative)?
- What are some justifications for [poor](sent_polarity:negative) outlook for [earnings](aspect_type:earnings)?


## intent:out_of_scope
- I want to order food
- Order me a pizza
- What is 2 + 2?
- Who’s the US President?
- I need a job
- I am asking you an out of scope question
- 4 + 2 = ?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- Are you ready?
- But you're an english site :(
- Can I ask you questions first?
- Can I die
- Can I get a hamburger?
- Can YouTube talk?
- Can you call me back ?
- Can you give me your datacenter's password
- Can you give me your datacenter's password?
- Can you make sandwiches?
- Can you please send me an uber
- Do I have to accept?
- Do you know Kevin Pelton
- Find nearest pizzahut
- Have we met before?
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- How long does it take to set up a Rasa bot?
- I already told you! I'm a shitmuncher
- I am User
- I am an opioid addic
- I am an opioid addict
- I am hungry
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- I can barely see this white text on light gray background ...
- I changed my mind
- I have installed it
- I ned a GP in 94301
- I need a GP in 94301
- I need a girl friend!
- I need to eat cake
- I wan to buy a plane
- I wanna marry you
- I want a new laptop
- I want book a hotel
- I want french cuisine
- I want pizza
- I want to die
- I want to order pizza
- I want to use pipe
- I'm a shitmuncher
- Is this Goal-Oriented Chatbot?
- Is today saturday?
- Mail me the guide
- Make me a sandwich
- NLW
- Nice name
- Now?
- Pizza bot
- Recharge
- SEL ME SOMETHING
- The Try it out is not working
- The weather is good
- Today
- Try it out broken
- What day is it today?
- What did you eat yesterday?
- What do you prefer?
- What is todays date
- What is your hobbies?
- What makes you better than a human?
- What's 1 + 1?
- What's do YouTube do
- What's your backend system?
- Where am I right now?
- Where am I?
- Who ?
- Who are your customers
- Why don’t you answer?
- Why is my TRUST score set to 50 after I completed the registration process?
- Won't you ask me how I am?
- You'r blue.
- Kristin, I want to marry you
- german?
- a tamed mouse will arrive at your doorstep in the next couple of days
- aRE YOU SINGLE
- again?
- alexa, order 5 tons of natrium chloride
- and make chicken noises into the phone
- are the newsletter worth the subscription?
- are u facebook
- are u, facebook?
- are you single?
- are you dev?
- are you human ?
- are you russian?
- are you sick
- are you using Rasa Core and NLU ?
- are you vegan
- book a ticket
- but I just told you that :(
- but if rasa is open source why do you have a sales team
- buy one please
- buy groceries
- call me father
- can we keep chatting?
- can you book dinner
- can you cheer me up
- can you cook dinner
- can you give me a cup of coffee
- can you help me with the docs?
- can you help me with your docs
- can you help me with your docs?
- can you learn from our conversation?
- can you speak about politic ?
- can you understand ?
- cannot see
- chgfhgh
- chinese ok?
- colder
- common, just try
- connect to alexa
- cr

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## synonym:sales
- revenue
- sales
- net revenue
- topline

## synonym:earnings
- net profit
- bottomline
- eps
- EPS 
- result
- net margin
- net margins
- profit margin

## synonym:op_costs
- opex
- operational cost
- operation cost
- operating cost
- operating costs
- operational expense
- operation expense
- expenses

## synonym:products_services
- products
- business
- business division
- biz
- products

## synonym:organic_expansion
- expansion
- expansion plans
- growth strategy

## synonym:acquisitions
- aquisition
- acquisituoin
- buyout
- M&A 
- mergers

## synonym:competition
- competitive landscape
- competitors

## synonym:op_risks
- risks
- business risks
- operational risk
- operation risk
- operating risk
- ops risks

## synonym:debt
- leverage
- gearing
- loan
- loans
- financing









