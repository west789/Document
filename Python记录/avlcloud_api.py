# test send bill async
def testEmail(request):
    from bill.tasks import email_bill
    email_bill()
    return JsonResponse({"test": 'OK'})

{
  allBooks {
    id
    title {
      id
      title
    }
    author {
      id
      name
    }
  }
}