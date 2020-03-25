## intent:greet
- good evening
- good morning

## intent:goodbye
- cya
- see you later
- goodbye

## intent:thanks
- Thank you
- Thank u

## intent:ask_what_can_u_do
- What can you do?
- How are you able to help me

## intent:inform
- [earnings](aspect_type)
- [sales](aspect_type)

## intent:query_sentiment
- Will I [make money](sent_polarity) from this stock this year?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Should we expect to see a net impact in [sales](aspect_type)?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- What is the general [tone](emot_polarity) of management?

## intent:query_sentence
- What are the primary drivers of [sales](aspect_type)?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- Are [earnings](aspect_type) performing in line with expectations?
- What's driving the more optimistic expectation for [sales](aspect_type)?

## intent:out_of_scope
- I am an opioid addic
- Can I ask you questions first?
- I need a GP in 94301
- I already told you! I'm a shitmuncher
- What makes you better than a human?
- but if rasa is open source why do you have a sales team
- buy one please
- are you russian?
- What's 1 + 1?
- again?
- can you learn from our conversation?
- can we keep chatting?
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- Who ?
- I need a girl friend!
- The weather is good
- Make me a sandwich
- can you give me a cup of coffee
- are you single?
- german?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- connect to alexa
- I want to order food
- I want to die

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
