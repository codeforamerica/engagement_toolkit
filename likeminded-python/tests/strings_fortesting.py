# coding=utf-8

"""
A module for keeping track of all the ugly xml and json strings used in testing.
"""

SEARCH_RESULTS_1 = """<search_results query="school" categories="2,6,32" subcategories="" type="All" status="All">
<results showing="4" available="1121">
<project>
<id>137</id>
<name><![CDATA[Tackling the achievement gap with a math competition]]></name><likeminded_url><![CDATA[likeminded.exygy.com/projects/tackling-the-achievement-gap-with-a-math-competition]]></likeminded_url>
</project>
<project>
<id>116</id>
<name><![CDATA[Combatting childhood obesity in Watsonville]]></name><likeminded_url><![CDATA[likeminded.exygy.com/projects/combatting-childhood-obesity-in-watsonville]]></likeminded_url>
</project>
<resource>
<id>1740</id>
<name><![CDATA[Links to Learning and Sustainability: Year Three Report of the Pennsylvania High School Coaching Initiative]]></name>
<likeminded_url><![CDATA[likeminded.exygy.com/resources/links-to-learning-and-sustainability-year-three-report-of-the-pennsylvania-high-school-coaching-init]]></likeminded_url>
</resource>
<resource>
<id>843</id>
<name><![CDATA[High Performance School Buildings: Energy-Smart Schools That Make a Difference]]></name>
<likeminded_url><![CDATA[likeminded.exygy.com/resources/high-performance-school-buildings-energy-smart-schools-that-make-a-difference]]></likeminded_url>
</resource>
</results>
</search_results>"""

SEARCH_RESULTS_2 = """<?xml version="1.0" encoding="UTF-8" ?><search_results query="ishkabibble" categories="" subcategories="" type="All" status="All"> 
	<results showing="0" available="0"> 
					</results> 
</search_results>"""

SEARCH_RESULTS_HIGH_SCHOOL_PG_1 = """<?xml version="1.0" encoding="UTF-8" ?><search_results query="high school" categories="" subcategories="" type="All" status="All"> 
	<results showing="10" available="11"> 
							<resource>	
				<id>686</id> 
				<name><![CDATA[Creating New Jobs, Cutting Carbon Emissions, and Reducing Oil Imports by Investing in Renewable Energy and Energy Efficiency]]></name> 
				<location><![CDATA[]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/creating-new-jobs-cutting-carbon-emissions-and-reducing-oil-imports-by-investing-in-renewable-energy]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>1956</id> 
				<name><![CDATA[SFGate - The California Academy of Sciences' beautiful new living-roof may well spark a revolution]]></name> 
				<location><![CDATA[]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/sfgate-the-california-academy-of-sciences-beautiful-new-living-roof-may-well-spark-a-revolution]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3201</id> 
				<name><![CDATA["Lean On Me" MLK Day of Service & Music]]></name> 
				<location><![CDATA[Oakland, California]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/lean-on-me-mlk-day-of-service-music]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>2741</id> 
				<name><![CDATA[Oakland Schools Become Neighborhood Produce Markets]]></name> 
				<location><![CDATA[Oakland, California]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/oakland-schools-become-neighborhood-produce-markets]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>2778</id> 
				<name><![CDATA[Golden Vision 2030]]></name> 
				<location><![CDATA[Golden, Colorado]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/golden-vision-2030]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3213</id> 
				<name><![CDATA[UAB article on Nutrition Boot Camp]]></name> 
				<location><![CDATA[Birmingham, Alabama]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/uab-article-on-nutrition-boot-camp]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3268</id> 
				<name><![CDATA[Recipes for Innovation in Public Engagement]]></name> 
				<location><![CDATA[]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/recipes-for-innovation-in-public-engagement]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3276</id> 
				<name><![CDATA[Maryland Fine Arts Instructional Tool Kit]]></name> 
				<location><![CDATA[]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/maryland-fine-arts-instructional-tool-kit]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3277</id> 
				<name><![CDATA[Maryland Fine Arts State Curriculum]]></name> 
				<location><![CDATA[]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/maryland-fine-arts-state-curriculum]]></likeminded_url> 
			</resource> 
					<resource>	
				<id>3536</id> 
				<name><![CDATA[ACCELERATING COLLEGE READINESS - LESSONS FROM NORTH CAROLINA’S INNOVATOR EARLY COLLEGES]]></name> 
				<location><![CDATA[Raleigh, North Carolina]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/accelerating-college-readiness-lessons-from-north-carolina-s-innovator-early-colleges]]></likeminded_url> 
			</resource> 
			</results> 
</search_results>"""

SEARCH_RESULTS_HIGH_SCHOOL_PG_2 = """<?xml version="1.0" encoding="UTF-8" ?><search_results query="high school" categories="" subcategories="" type="All" status="All"> 
	<results showing="1" available="11"> 
							<resource>	
				<id>3752</id> 
				<name><![CDATA[Article Describing the Debate Club Mission and Charter]]></name> 
				<location><![CDATA[Reno, Nevada]]></location> 
				<likeminded_url><![CDATA[likeminded.exygy.com/resource/article-describing-the-debate-club-mission-and-charter]]></likeminded_url> 
			</resource> 
			</results> 
</search_results>"""

SEARCH_RESULTS_HIGH_SCHOOL_PG_3 = """<?xml version="1.0" encoding="UTF-8" ?><search_results query="high school" categories="" subcategories="" type="All" status="All"> 
	<results showing="0" available="11"> 
					</results> 
</search_results>"""

PROJECT_193 = """<?xml version="1.0" encoding="UTF-8" ?> 
<project><name><![CDATA[Saving for Education]]></name><start_date /><end_date /><status>2</status><problem><![CDATA[A woman not having enough money to pay for her teenage daughter's extracurricular activities at school]]></problem><process><![CDATA[A single mother, Dametra worked full-time while living in a homeless shelter, building up enough money to rent a bad apartment in a worse neighborhood. Her daughter, Yvonne, risked losing a private scholarship due to poor grades. Hope was in short supply.<br><br><br /> 
Then Dametra joined EARN, where she created a spending plan and set savings goals for her future. Eventually, Dametra saved enough money to hire a much-needed tutor for Yvonne, securing the grade-based scholarship that was keeping the teenager enrolled at a private high school.<br><br><br /> 
Soon after, Dametra herself earned a private scholarship to Mills College — and, I’m excited to say, recently graduated. She’s now starting her own business in the Bay Area.]]></process><result><![CDATA[Yvonne has been offered scholarships to multiple colleges, and Dametra is running a successful business.]]></result><created><![CDATA[2011-03-14 20:45:26]]></created><updated><![CDATA[2011-03-17 15:07:42]]></updated><external_feed_account /><id>193</id><link><![CDATA[http://likeminded.exygy.com/project/saving-for-education]]></link><locations><location><id>0</id><slug /><zipcode /><city><![CDATA[San Francisco, California]]></city><county /><state_name /><state_prefix /><area_code /><time_zone /><lat /><lon /><created><![CDATA[2011-03-14 20:45:26]]></created><updated><![CDATA[2011-03-14 20:45:26]]></updated><is_free_text>1</is_free_text></location></locations><resources /><categories><category><![CDATA[Economy]]></category><category><![CDATA[Personal Finance]]></category></categories></project>"""

PROJECT_124 = """<?xml version="1.0" encoding="UTF-8" ?> 
<project><name><![CDATA[From crime-ridden to community center]]></name><start_date><![CDATA[01/01/2001]]></start_date><end_date /><status>1</status><problem><![CDATA[Five years ago, there wasn’t much reason to walk down Aleppo Street in the Olneyville neighborhood of Providence, RI, unless you were looking for trouble. Amid the rotting mill buildings between the street and the river, drug dealers and prostitutes did a steady business. The blocks surrounding Aleppo Street were the worst by far.]]></problem><process><![CDATA[A series of innovative collaborations between residents, local non-profits, and city agencies, including the police department, transformed the crime-ridden riverfront into a center of community life.<br /> 
<br /> 
The neighborhood’s victory lies not just in the creation of a new park but also in the innovative strategy that reduced crime and made it a safe place to be. That strategy was carried out largely through an unconventional alliance between a housing development corporation and local police, with support from Rhode Island LISC.<br /> 
<br /> 
Working with Olneyville Housing Corporation changed the way local police thought about their job, said Lt. Dean Isabella, commander of the local police district. “It made us a part of developing a community as opposed to just policing it,” he said.<br /> 
<br /> 
The story began in 2001 when Frank Shea, executive director of Olneyville Housing Corporation, organized a dozen neighborhood groups and won a state grant to plan neighborhood improvements, including housing and recreation. The city had already begun to remediate the toxic riverfront and promised to install a park that the neighborhood had long wanted.<br /> 
]]></process><result><![CDATA[Today, Riverside Park --- a lynchpin in the neighborhood transformation --– draws picnickers, dog-walkers and soccer players. Bicyclists cruise down a paved trail that snakes for miles in either direction. Children swing and climb in the play lot. Last October, during Olneyville's Fall Festival, neighbors danced in the grassy field to salsa and merengue. Since 2002, reported crime in the redeveloped area has fallen by 60 percent. ]]></result><created><![CDATA[2011-02-15 13:12:32]]></created><updated><![CDATA[2011-02-15 18:09:16]]></updated><external_feed_account /><id>124</id><link><![CDATA[http://likeminded.exygy.com/project/from-crime-ridden-to-community-center]]></link><locations><location><id>976</id><slug><![CDATA[providence-ri]]></slug><zipcode>02901</zipcode><city><![CDATA[Providence]]></city><county><![CDATA[Providence]]></county><state_name><![CDATA[Rhode Island]]></state_name><state_prefix><![CDATA[RI]]></state_prefix><area_code>401</area_code><time_zone><![CDATA[Eastern]]></time_zone><lat>41.8268</lat><lon>-71.408</lon><created /><updated><![CDATA[2011-01-22 14:39:09]]></updated><is_free_text>0</is_free_text></location></locations><resources /><categories><category><![CDATA[Crime & Safety]]></category><category><![CDATA[Prevention]]></category></categories></project>"""

RESOURCE_200 = """<?xml version="1.0" encoding="UTF-8" ?> 
<resource><name><![CDATA[Gaining Ground: Supporting English Learners Through After-School Literacy Programming]]></name><description><![CDATA[This brief presents findings that demonstrate a relationship between key approaches in CORAL, an eight-year, $58 million after-school initiative of The James Irvine Foundation, and the academic progress of English learners. In addition to presenting findings, the brief suggests important considerations for any policymaker and funder interested in the success of English learners as a growing student population.]]></description><url><![CDATA[http://www.issuelab.org/data_partners/likeminded/gaining_ground_supporting_english_learners_through_after_school_literacy_programming]]></url><created><![CDATA[2011-01-21 19:30:30]]></created><updated><![CDATA[2011-01-21 19:30:30]]></updated><id>200</id><author><![CDATA[IssueLab]]></author><link><![CDATA[http://likeminded.exygy.com/resource/gaining-ground-supporting-english-learners-through-after-school-literacy-programming]]></link><locations /><projects /></resource>"""
