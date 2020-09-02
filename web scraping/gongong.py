from lxml import html
import requests
page = requests.get('https://docs.google.com/forms/d/e/1FAIpQLSdttZHfHo9QADrt-OxUQc_MdnU0R9YDum05C7ZR91ohn5NuoA/viewform')
tree = html.fromstring(page.content)
#answers = tree.xpath('//div[@class="quantumWizTogglePaperradioEl docssharedWizToggleLabeledControl freebirdThemedRadio freebirdThemedRadioDarkerDisabled freebirdFormviewerViewItemsRadioControl"]/@data-value')
answers = tree.xpath('//div[@data-value="Gonggong"]//div[@class="quantumWizTogglePaperradioRadioContainer"]/div[@class="quantumWizTogglePaperradioOffRadio exportOuterCircle"]/@class')

for i in answers:
    print(i)
