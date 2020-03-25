## intent:greet
- Hey
- hey there
- hello
- good morning
- Hello
- hey

## intent:goodbye
- goodbye
- see ya
- goodnight
- see you around
- cya
- bye bye
- farewell

## intent:thanks
- Thank you
- Thanks for that
- thnaks
- Thank you so much

## intent:ask_what_can_u_do
- What can you do
- help
- help me
- What can you do?
- How can you help me?

## intent:inform
- [op_costs](aspect_type)
- [organic_expansion](aspect_type)
- [debt](aspect_type)
- [products_services](aspect_type)
- [earnings](aspect_type)
- [op_risks](aspect_type)

## intent:query_sentiment
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- What is the [outlook](sent_polarity) for share price of the company?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Will growth rate be expected to reaccelerate from here?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- Is company expected to be active on the merger and acquistion front this year?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- How is the company performing vs our [competitors](aspect_type:competition)?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- How are company's [expenses](aspect_type:op_costs) trending?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- What is the overall [outlook](sent_polarity) for the company as a whole?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- Is management [optimistic](emot_polarity)?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- So should we expect a reversal or a benefit in the fourth quarter?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- Will I [make money](sent_polarity) from this stock this year?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?

## intent:query_sentence
- What's driving the more optimistic expectation for [sales](aspect_type)?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- Why have [sales](aspect_type) not been up to expectations?
- What is holding back the [sales](aspect_type) growth this quarter?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- Are [earnings](aspect_type) performing in line with expectations?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?

## intent:out_of_scope
- Do I have to accept?
- I need a girl friend!
- are you single?
- I already told you! I'm a shitmuncher
- and make chicken noises into the phone
- Why is my TRUST score set to 50 after I completed the registration process?
- I want to order food
- I changed my mind
- can you learn from our conversation?
- a tamed mouse will arrive at your doorstep in the next couple of days
- can you give me a cup of coffee
- What did you eat yesterday?
- Can you give me your datacenter's password?
- I am asking you an out of scope question
- I am an opioid addict
- I need a job
- Recharge
- Who ?
- Who are your customers
- I need to eat cake
- are you sick
- are you vegan
- are u, facebook?
- common, just try
- I can barely see this white text on light gray background ...
- NLW
- What's 1 + 1?
- Where am I?
- connect to alexa
- buy one please
- I want a new laptop
- Have we met before?
- Do you know Kevin Pelton
- What's your backend system?
- are u facebook
- Can you make sandwiches?
- chinese ok?
- What is 2 + 2?
- Why don’t you answer?
- I wanna marry you
- buy groceries
- are the newsletter worth the subscription?
- You'r blue.
- SEL ME SOMETHING
- What is your hobbies?
- cr
- Pizza bot
- I want book a hotel
- I am an opioid addic
- I ned a GP in 94301
- Won't you ask me how I am?
- I want to use pipe
- are you dev?
- chgfhgh
- What day is it today?
- Can YouTube talk?
- can you help me with the docs?
- I have installed it
- Nice name
- call me father
- I wan to buy a plane
- What is todays date
- Kristin, I want to marry you
- I want to die
- Can I ask you questions first?
- cannot see
- I want pizza
- book a ticket
- can you cheer me up
- german?
- can you cook dinner
- but I just told you that :(

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
