def test_read_model(self):
    model = YourModel.objects.create(field1='value1', field2='value2')
    retrieved_model = YourModel.objects.get(id=model.id)
    self.assertEqual(retrieved_model.field1, 'value1')
    self.assertEqual(retrieved_model.field2, 'value2')
    
