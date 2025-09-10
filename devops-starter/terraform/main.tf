# This is a minimal stub to show structure. For a full EKS setup,
# integrate modules like terraform-aws-modules/eks/aws.
# Keeping this lightweight to avoid surprise costs.
resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.cluster_name}-artifacts"
}
output "artifacts_bucket" {
  value = aws_s3_bucket.artifacts.bucket
}
