####################
# ELB
####################
resource "aws_elb" "elb" {
  name = "elb-${var.environment}-${var.name}"
  security_groups = var.security_group
  subnets = var.subnet_ids
  internal = false
  cross_zone_load_balancing = true
  connection_draining = true
  connection_draining_timeout = 300
  dynamic "listener" {
    for_each = var.listeners
    content {
      lb_protocol        = listener.value.lb_protocol
      lb_port            = listener.value.lb_port
      instance_protocol  = listener.value.instance_protocol
      instance_port      = listener.value.instance_port
      ssl_certificate_id = listener.value.ssl_certificate_id
    }
  }
  health_check {
    target = var.health_check_target
    healthy_threshold = 10
    unhealthy_threshold = 10
    timeout = 15
    interval = 30
  }
  tags = merge(tomap({NName = "elb-${var.environment}-${var.name}"}), var.tags)
}
