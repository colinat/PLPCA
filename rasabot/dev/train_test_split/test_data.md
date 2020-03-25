## intent:greet
- hi
- Hey

## intent:goodbye
- cya
- bye
- gotta go

## intent:thanks
- Thank you
- thnaks

## intent:ask_what_can_u_do
- What can you do
- help

## intent:inform
- [debt](aspect_type)
- [sales](aspect_type)

## intent:query_sentiment
- Is CEO [optimistic](emot_polarity:confident) about 2020 for the company
- Is management [optimistic](emot_polarity:confident)?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- Is there expectation for growth to moderate?
- Have interest rate trends benefited/acted against the company?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- How far can [stock price](aspect_type:earnings) go this year?
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company

## intent:query_sentence
- What are some justifications for [poor](sent_polarity:negative) outlook for [earnings](aspect_type)?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- I wish to know what CEO said about our company outlook for [earnings](aspect_type)?
- What is management saying about our [competitors](aspect_type:competition)?
- Should we expect to see a net impact in margin?
- What are some management comments on the [bullish](emot_polarity:confident) [earnings](aspect_type) [outlook](sent_polarity)?
- Why is the CEO [upbeat](sent_polarity:positive) on [earnings](aspect_type)?
- What are some of CEO's views on potential [market share](aspect_type:organic_expansion) increase?

## intent:out_of_scope
- I am hungry
- I can barely see this white text on light gray background ...
- 4 + 2 = ?
- Can you please send me an uber
- aRE YOU SINGLE
- Now?
- I want to order food
- are u, facebook?
- and make chicken noises into the phone
- What is todays date
- can you help me with your docs?
- can you learn from our conversation?
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- can you understand ?
- How long does it take to set up a Rasa bot?
- I need a job
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- are you hungry?
- are you dev?
- but I just told you that :(
- cr
- can you speak about politic ?
- Can YouTube talk?
- Are you ready?
- Who are your customers

## intent:bot_challenge
- am I talking to a bot?

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
- bullish
- optimism

## synonym:debt
- gearing
- leverage
- geared
- liquidity
- financing
- borrowings
- interest costs
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
- unexpected
- rising costs
- bearish
- bad
- poor

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
- market share
- expansion
- expansion plans
- growth strategy

## synonym:positive
- favourable
- upbeat
- exciting
- positive opinion

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
