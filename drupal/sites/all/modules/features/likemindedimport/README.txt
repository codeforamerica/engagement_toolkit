This feature provides

To import our LikeMinded CouchDB, on another site, do the following.

1. Install this feature.
2. Create a new "LikemindedSource" content type page.
node/add/likemindedsource

3. Add this URL in the URL field (which points to our pheattle couchDB)

http://pheattle.iriscouch.com/likeminded_projects/_design/projects/_view/all

4. In JSONPATH PARSER SETTINGS

Provide the values to parse the JSON document.

context:
$.rows.*

field_problem
value.problem

field_process
value.process

field_result
value.result

title:
value.name

5. Updating the import.
As you add new fields, you can map categories, links and other features. 

Edit the feed:
admin/structure/feeds/edit/likeminded

Change the mapping:
admin/structure/feeds/edit/likeminded/mapping

Add a new source (JSONPath Expression) and map it to your field.


### An Example of a Couch resource

From:
http://pheattle.iriscouch.com/_utils/document.html?likeminded_projects/e73dafceef7641d4f860bb9f5d3fa544

_id	e73dafceef7641d4f860bb9f5d3fa544
_rev	1-b5f278ccf7c1e7ed8d979cb46d330cad
created	2011-02-03 16:21:03
end_date	{ }
external_feed_account	{ }
id	75
link	http://likeminded.org/project/organize-a-food-drive-for-awareness
locations	

location

name	Organize a Food Drive for Awareness
opencalais	

doc
topics
entities

problem	Local food banks and soup kitchens need help raising donations and awareness for their causes.
process	HOA members in the Edgewood neighborhood organized a canned food drive in a nearby park. Weeks before setting up the food drive itself, the ...
resources	{ }
result	{ }
start_date	{ }
status	1
updated