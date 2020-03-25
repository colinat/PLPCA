## intent:greet
- hey
- hi again
- good evening
- hey there
- Hello
- good morning

## intent:goodbye
- bye
- cya
- good night
- see you around
- see you later
- gotta go
- goodnight

## intent:thanks
- Thank you so much
- Thank u
- Thank you
- Thanks

## intent:ask_what_can_u_do
- How are you able to help me
- help me
- What can you do
- what can u do
- What can you do?

## intent:inform
- [organic_expansion](aspect_type)
- [products_services](aspect_type)
- [earnings](aspect_type)
- [acquisitions](aspect_type)
- [op_costs](aspect_type)
- [sales](aspect_type)

## intent:query_sentiment
- What is the overall [outlook](sent_polarity) for the company as a whole?
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Will I [make money](sent_polarity) from this stock this year?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- How have our [acquisitions](aspect_type) performed?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Is management [optimistic](emot_polarity)?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- Should we expect to see a net impact in [sales](aspect_type)?
- How is the company's balance sheet and [debt](aspect_type) level?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- How far can [stock price](aspect_type:earnings) go this year?
- Can we expect to see accelerating return from the investments?
- What is the general [tone](emot_polarity) of management?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- So should we expect a reversal or a benefit in the fourth quarter?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- Is there expectation for growth to moderate?

## intent:query_sentence
- What caused margin [to decline](sent_polarity:negative)?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Are [earnings](aspect_type) performing in line with expectations?
- Why have [sales](aspect_type) not been up to expectations?
- What is holding back the [sales](aspect_type) growth this quarter?
- What's driving the more optimistic expectation for [sales](aspect_type)?
- Any changes in the [sales](aspect_type) trends?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?

## intent:out_of_scope
- Won't you ask me how I am?
- Who ?
- I changed my mind
- but if rasa is open source why do you have a sales team
- I want french cuisine
- again?
- chgfhgh
- You'r blue.
- buy one please
- Today
- are you sick
- NLW
- are you human ?
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- What is your hobbies?
- connect to alexa
- Who’s the US President?
- I am User
- Can you please send me an uber
- I'm a shitmuncher
- Kristin, I want to marry you
- What is todays date
- can you cook dinner
- Can you call me back ?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- What day is it today?
- can you book dinner
- But you're an english site :(
- are you russian?
- book a ticket
- but I just told you that :(
- I already told you! I'm a shitmuncher
- Is today saturday?
- aRE YOU SINGLE
- german?
- What did you eat yesterday?
- Recharge
- are you single?
- chinese ok?
- common, just try
- I am asking you an out of scope question
- Find nearest pizzahut
- Can I get a hamburger?
- I want a new laptop
- can you cheer me up
- can we keep chatting?
- I wanna marry you
- I can barely see this white text on light gray background ...
- alexa, order 5 tons of natrium chloride
- Can you give me your datacenter's password
- I am hungry
- Nice name
- I want to order food
- Mail me the guide
- Can YouTube talk?
- can you learn from our conversation?
- The Try it out is not working
- Have we met before?
- Make me a sandwich
- I want to order pizza
- What do you prefer?
- Now?
- I am an opioid addic
- I want pizza
- Can you give me your datacenter's password?
- Do I have to accept?
- are u facebook
- I have installed it
- Is this Goal-Oriented Chatbot?
- What's your backend system?
- I ned a GP in 94301
- are u, facebook?

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
