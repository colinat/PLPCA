## intent:greet
- hey
- good morning
- good evening

## intent:goodbye
- bye
- see you later
- goodnight
- see you around

## intent:thanks
- Thank you so much
- Thank you

## intent:ask_what_can_u_do
- What can you do?
- What can you do
- help me

## intent:inform
- [organic_expansion](aspect_type)
- [acquisitions](aspect_type)
- [earnings](aspect_type)

## intent:query_sentiment
- So should we expect a reversal or a benefit in the fourth quarter?
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- What is the general [tone](emot_polarity) of management?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Is there expectation for growth to moderate?
- How far can [stock price](aspect_type:earnings) go this year?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Is management [optimistic](emot_polarity)?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- Will I [make money](sent_polarity) from this stock this year?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Can we expect to see accelerating return from the investments?
- How is the company performing vs our [competitors](aspect_type:competition)?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company

## intent:query_sentence
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Why have [sales](aspect_type) not been up to expectations?
- What's driving the more optimistic expectation for [sales](aspect_type)?
- Are [earnings](aspect_type) performing in line with expectations?
- What caused margin [to decline](sent_polarity:negative)?

## intent:out_of_scope
- Mail me the guide
- are you russian?
- Is today saturday?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- Have we met before?
- I changed my mind
- common, just try
- The Try it out is not working
- Today
- I am asking you an out of scope question
- Make me a sandwich
- are you sick
- can you book dinner
- again?
- alexa, order 5 tons of natrium chloride
- I'm a shitmuncher
- can you cheer me up
- are u, facebook?
- can you learn from our conversation?
- Who ?
- are you single?
- Can you give me your datacenter's password?
- NLW
- What did you eat yesterday?
- I have installed it
- I ned a GP in 94301
- Is this Goal-Oriented Chatbot?
- Won't you ask me how I am?
- but if rasa is open source why do you have a sales team
- I wanna marry you
- connect to alexa
- What's your backend system?
- I am User
- Now?
- You'r blue.
- aRE YOU SINGLE

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
