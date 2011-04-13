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

CATEGORIES = """<?xml version="1.0" encoding="UTF-8" ?> 
<categories><category><id>1</id><name><![CDATA[Arts]]></name></category><sub_categories><id>2</id><name><![CDATA[Museums]]></name><category_id>1</category_id></sub_categories><sub_categories><id>4</id><name><![CDATA[Performing Arts]]></name><category_id>1</category_id></sub_categories><sub_categories><id>5</id><name><![CDATA[Public]]></name><category_id>1</category_id></sub_categories><sub_categories><id>6</id><name><![CDATA[Visual Arts]]></name><category_id>1</category_id></sub_categories><category><id>2</id><name><![CDATA[Health]]></name></category><sub_categories><id>8</id><name><![CDATA[Addiction]]></name><category_id>2</category_id></sub_categories><sub_categories><id>9</id><name><![CDATA[Disability]]></name><category_id>2</category_id></sub_categories><sub_categories><id>10</id><name><![CDATA[Food & Nutrition]]></name><category_id>2</category_id></sub_categories><sub_categories><id>11</id><name><![CDATA[Health Care]]></name><category_id>2</category_id></sub_categories><sub_categories><id>12</id><name><![CDATA[Mental Health]]></name><category_id>2</category_id></sub_categories><sub_categories><id>13</id><name><![CDATA[Obesity]]></name><category_id>2</category_id></sub_categories><sub_categories><id>14</id><name><![CDATA[Recreation/Sports]]></name><category_id>2</category_id></sub_categories><category><id>3</id><name><![CDATA[Education]]></name></category><sub_categories><id>15</id><name><![CDATA[Arts]]></name><category_id>3</category_id></sub_categories><sub_categories><id>16</id><name><![CDATA[Technology]]></name><category_id>3</category_id></sub_categories><sub_categories><id>17</id><name><![CDATA[Language]]></name><category_id>3</category_id></sub_categories><sub_categories><id>18</id><name><![CDATA[Libraries]]></name><category_id>3</category_id></sub_categories><sub_categories><id>19</id><name><![CDATA[Literacy]]></name><category_id>3</category_id></sub_categories><sub_categories><id>20</id><name><![CDATA[Public Schools]]></name><category_id>3</category_id></sub_categories><category><id>4</id><name><![CDATA[Crime & Safety]]></name></category><sub_categories><id>22</id><name><![CDATA[Domestic]]></name><category_id>4</category_id></sub_categories><sub_categories><id>23</id><name><![CDATA[Drugs]]></name><category_id>4</category_id></sub_categories><sub_categories><id>24</id><name><![CDATA[Prevention]]></name><category_id>4</category_id></sub_categories><sub_categories><id>26</id><name><![CDATA[Violent Crime]]></name><category_id>4</category_id></sub_categories><category><id>5</id><name><![CDATA[Environment]]></name></category><sub_categories><id>27</id><name><![CDATA[Energy]]></name><category_id>5</category_id></sub_categories><sub_categories><id>28</id><name><![CDATA[Farming]]></name><category_id>5</category_id></sub_categories><sub_categories><id>29</id><name><![CDATA[Pollution]]></name><category_id>5</category_id></sub_categories><sub_categories><id>30</id><name><![CDATA[Preservation]]></name><category_id>5</category_id></sub_categories><sub_categories><id>31</id><name><![CDATA[Recycling]]></name><category_id>5</category_id></sub_categories><sub_categories><id>33</id><name><![CDATA[Wildlife]]></name><category_id>5</category_id></sub_categories><category><id>6</id><name><![CDATA[Economy]]></name></category><sub_categories><id>34</id><name><![CDATA[Economic Development]]></name><category_id>6</category_id></sub_categories><sub_categories><id>35</id><name><![CDATA[Job Training]]></name><category_id>6</category_id></sub_categories><sub_categories><id>36</id><name><![CDATA[Personal Finance]]></name><category_id>6</category_id></sub_categories><sub_categories><id>38</id><name><![CDATA[Small Business]]></name><category_id>6</category_id></sub_categories><sub_categories><id>39</id><name><![CDATA[Unemployment]]></name><category_id>6</category_id></sub_categories><category><id>7</id><name><![CDATA[Government]]></name></category><sub_categories><id>40</id><name><![CDATA[Civic Participation]]></name><category_id>7</category_id></sub_categories><sub_categories><id>42</id><name><![CDATA[Local Politics]]></name><category_id>7</category_id></sub_categories><sub_categories><id>43</id><name><![CDATA[Planning]]></name><category_id>7</category_id></sub_categories><sub_categories><id>44</id><name><![CDATA[Public Safety]]></name><category_id>7</category_id></sub_categories><sub_categories><id>45</id><name><![CDATA[Transportation]]></name><category_id>7</category_id></sub_categories><category><id>8</id><name><![CDATA[Community]]></name></category><sub_categories><id>52</id><name><![CDATA[Family]]></name><category_id>8</category_id></sub_categories><sub_categories><id>47</id><name><![CDATA[Children]]></name><category_id>8</category_id></sub_categories><sub_categories><id>48</id><name><![CDATA[Housing]]></name><category_id>8</category_id></sub_categories><sub_categories><id>49</id><name><![CDATA[Aging]]></name><category_id>8</category_id></sub_categories><sub_categories><id>50</id><name><![CDATA[Diversity]]></name><category_id>8</category_id></sub_categories><sub_categories><id>51</id><name><![CDATA[Recreation]]></name><category_id>8</category_id></sub_categories></categories>"""
