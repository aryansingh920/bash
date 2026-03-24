resource "local_file" "pet_name" {
  filename = "my_pet.txt"
  content  = "My pet's name is Fluffy"
  lifecycle {
    ignore_changes = [content]
  }
}

resource "null_resource" "logic_test" {
  triggers = {
    test_value = "This is just a test"
  }
}
