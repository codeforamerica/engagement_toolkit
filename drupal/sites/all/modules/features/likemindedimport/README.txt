This feature provides

To import our LikeMinded CouchDB, on another site, do the following.

1. Install this feature.
2. Create a new "LikemindedSource" content type page.
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