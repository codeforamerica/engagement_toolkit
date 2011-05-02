require 'CSV'
require 'rbing'
require 'time'

domain = 'phila.gov'

bing = RBing.new("248A1D8594169FE22B8F3D5BDB8F6C19141FD2F5")
g = []
a = 0
# Only allows 1000 results, which is 20 pages * 50 results per page
while a != 20
  rsp = bing.web('(site:'+domain+') "Frequently Asked Questions"', {:count => 50, :offset => a})
  rsp["Web"]["Results"].each do |x|
    g << x["Url"]
  end
  a = a + 1
  puts a
end

puts g.size
puts g.uniq.size

# Only allows 1000 results, which is 20 pages * 50 results per page
exclusion = ""
g.uniq[0..20].map { |x| exclusion = exclusion + ' -"' + x +'"'}
a = 0
puts exclusion
while a != 20
  rsp = bing.web('(site:'+domain+') "Frequently Asked Questions"' + exclusion, {:count => 50, :offset => a})
  rsp["Web"]["Results"].each do |x|
    g << x["Url"] unless g.include?(x["Url"])
  end
  a = a + 1
  puts a
end

ts = Time.now.strftime("%Y%m%d_%H%M%S")
CSV.open("/Users/mertonium/Code/engagement_toolkit/qa/faq_scraper/bing_results/reuslts_#{ts}.csv", "w") do |csv|
  g.each do |x|
    csv << [x]
  end
end