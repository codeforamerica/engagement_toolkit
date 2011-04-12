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

