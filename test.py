# test.py
from fluent import sender
from fluent import event
sender.setup('mytester', host='localhost', port=24225)
event.Event('follow', {
  'from': 'userA',
  'to':   'userB'
})
