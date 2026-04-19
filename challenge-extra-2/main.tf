locals {
  prefix         = "${path.module}/${var.manifests_folder}"
  manifest_paths = fileset(local.prefix, "**/*.yml")
  manifests_raw  = [for data in flatten([for path in local.manifest_paths : split("---", file("${local.prefix}/${path}"))]) : data]
  manifests_decoded = {for k, v in local.manifests_raw: "${lower(yamldecode(v).kind)}/${yamldecode(v).metadata.name}" => yamldecode(v)}
}

resource "kubernetes_manifest" "manifests" {
  for_each = local.manifests_decoded
  manifest = each.value
}