# Infraestructura de PRUEBA con malas configuraciones para validar Checkov
resource "aws_db_instance" "prueba" {
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  publicly_accessible = true
  storage_encrypted   = false
}
